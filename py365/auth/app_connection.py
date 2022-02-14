from abc import ABC
from enum import Enum
from typing import Optional, Any
from urllib import parse

from pydantic import BaseModel


class CallMethod(str, Enum):
    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
    DELETE = "DELETE"


class GraphResponse(BaseModel):
    status_code: int
    headers: Optional[dict] = None
    content: Optional[bytes] = None
    text: Optional[str] = None
    json: Optional[Any] = None

    @property
    def ok(self) -> bool:
        return self.status_code == "201"


class AppConnection(ABC):
    def __init__(self, resource, api_ver):
        self.resource = resource
        self.api_base_url = f"{self.resource}/{api_ver}/"

    def get_api_url(self, endpoint: str):
        """Convert a relative path such as /me/photo/$value to a full URI
        This is much easier to work with how MS are actually documenting their API
        """
        if parse.urlparse(endpoint).scheme in ["http", "https"]:
            return endpoint  # url is already complete
        return parse.urljoin(self.api_base_url, endpoint.lstrip("/"))

    def request_from_graph(
        self,
        method: CallMethod,
        url: str,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        headers: Optional[dict] = None,
    ) -> GraphResponse:
        raise NotImplementedError("pure function")

    def get(self, endpoint: str, params: dict) -> GraphResponse:
        url = self.get_api_url(endpoint=endpoint)
        response = self.request_from_graph(
            method=CallMethod.GET, url=url, params=params
        )
        return response

    def post(
        self, endpoint: str, data: dict, headers: Optional[dict] = None
    ) -> GraphResponse:
        url = self.get_api_url(endpoint=endpoint)
        response = self.request_from_graph(
            method=CallMethod.POST, url=url, data=data, headers=headers
        )
        return response

    def patch(
        self, endpoint: str, data: dict, headers: Optional[dict] = None
    ) -> GraphResponse:
        url = self.get_api_url(endpoint=endpoint)
        response = self.request_from_graph(
            method=CallMethod.PATCH, url=url, data=data, headers=headers
        )
        return response

    def delete(self, endpoint: str, headers: Optional[dict] = None) -> GraphResponse:
        url = self.get_api_url(endpoint=endpoint)
        response = self.request_from_graph(
            method=CallMethod.DELETE, url=url, headers=headers
        )
        return response
