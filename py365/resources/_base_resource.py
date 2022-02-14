import urllib.parse
from typing import Optional

from py365.auth import AppConnection, GraphResponse
from py365.data import BaseData


class BaseResource:
    """
    Represent a base resource API on the OG
    Every OG API class should inherit from this class
    """

    def __init__(self, connection: AppConnection, edge_base):
        self._connection: AppConnection = connection
        self.EDGE_BASE = edge_base

    @staticmethod
    def __get_response_data__(data: BaseData, response: GraphResponse):
        if data and response.ok:
            if response.text:
                json = response.json()
                data.parse_raw(json)
            if "ETag" in response.headers:
                data.eTag = response.headers["ETag"]

    def __get_api__(
        self,
        edge_end: str = "",
        params: dict = None,
        return_data: BaseData = None,
    ) -> GraphResponse:
        endpoint = self.EDGE_BASE + edge_end
        endpoint = urllib.parse.quote(endpoint)
        response = self._connection.get(endpoint=endpoint, params=params)
        self.__get_response_data__(return_data, response)
        return response

    def __post_api__(
        self,
        edge_end: str = "",
        data: Optional[dict] = None,
        post_data: Optional[BaseData] = None,
        return_data: Optional[BaseData] = None,
    ) -> GraphResponse:
        endpoint = self.EDGE_BASE + edge_end
        endpoint = urllib.parse.quote(endpoint)
        headers = {}
        if post_data:
            data = post_data.json
            if post_data.eTag:
                headers.update({"If-Match": post_data.eTag})
        response = self._connection.post(endpoint=endpoint, data=data, headers=headers)
        self.__get_response_data__(return_data, response)
        return response

    def __patch_api__(
        self,
        edge_end: str = "",
        json: Optional[dict] = None,
        patch_data: Optional[BaseData] = None,
        return_data: Optional[BaseData] = None,
    ) -> GraphResponse:
        endpoint = self.EDGE_BASE + edge_end
        endpoint = urllib.parse.quote(endpoint)
        headers = {}
        if patch_data:
            json = patch_data.json
            if patch_data.eTag:
                headers.update({"If-Match": patch_data.eTag})
        response = self._connection.patch(endpoint=endpoint, data=json, headers=headers)
        self.__get_response_data__(return_data, response)
        return response

    def __delete_api__(
        self, edge_end: str = "", delete_data: Optional[BaseData] = None
    ):
        endpoint = self.EDGE_BASE + edge_end
        endpoint = urllib.parse.quote(endpoint)
        headers = {}
        if delete_data:
            if delete_data.eTag:
                headers.update({"If-Match": delete_data.eTag})
        response = self._connection.delete(endpoint=endpoint, headers=headers)
        return response
