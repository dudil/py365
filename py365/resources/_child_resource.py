from typing import Optional

from py365.data import BaseData
from ._base_resource import BaseResource, GraphResponse


class ChildResource:
    """
    Represent a child resource on the OG
    Every OG API class that represent a child API should inherit from this class
    """

    def __init__(self, base_api: BaseResource, edge_mid: str):
        self.baseAPI: BaseResource = base_api
        self.edge_mid = edge_mid

    def __get_api__(
        self,
        edge_end: str = "",
        params: Optional[dict] = None,
        return_data: Optional[BaseData] = None,
    ) -> GraphResponse:
        edge = self.edge_mid + edge_end
        response = self.baseAPI.__get_api__(
            edge_end=edge, params=params, return_data=return_data
        )
        return response

    def __post_api__(
        self,
        edge_end: str = "",
        data: Optional[dict] = None,
        post_data: Optional[BaseData] = None,
        return_data: Optional[BaseData] = None,
    ) -> GraphResponse:
        edge = self.edge_mid + edge_end
        response = self.baseAPI.__post_api__(
            edge_end=edge,
            data=data,
            post_data=post_data,
            return_data=return_data,
        )
        return response

    def __patch_api__(
        self,
        edge_end: str = "",
        data: Optional[dict] = None,
        patch_data: Optional[BaseData] = None,
        return_data: Optional[BaseData] = None,
    ) -> GraphResponse:
        edge = self.edge_mid + edge_end
        response = self.baseAPI.__patch_api__(
            edge_end=edge,
            json=data,
            patch_data=patch_data,
            return_data=return_data,
        )
        return response

    def __delete_api__(
        self, edge_end: str = "", delete_data: Optional[BaseData] = None
    ):
        edge = self.edge_mid + edge_end
        response = self.baseAPI.__delete_api__(edge_end=edge, delete_data=delete_data)
        return response
