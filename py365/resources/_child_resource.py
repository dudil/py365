from requests import Response
from py365.data import BaseData
from ._base_resource import BaseResource


class ChildResource:
    """
    Represent a child resource on the OG
    Every OG API class that represent a child API should inherit from this class
    """

    def __init__(self, baseAPI: BaseResource, edgeMid: str):
        self.baseAPI: BaseResource = baseAPI
        self.edgeMid = edgeMid

    def __getAPI__(
        self,
        edgeEnd: str = "",
        params: dict = None,
        permissions: [str] = None,
        returnData: BaseData = None,
    ) -> Response:
        edge = self.edgeMid + edgeEnd
        response = self.baseAPI.__getAPI__(
            edgeEnd=edge, params=params, permissions=permissions, returnData=returnData
        )
        return response

    def __postAPI__(
        self,
        edgeEnd: str = "",
        json: dict = None,
        permissions: [str] = None,
        postData: BaseData = None,
        returnData: BaseData = None,
    ) -> Response:
        edge = self.edgeMid + edgeEnd
        response = self.baseAPI.__postAPI__(
            edgeEnd=edge,
            json=json,
            permissions=permissions,
            postData=postData,
            returnData=returnData,
        )
        return response

    def __patchAPI__(
        self,
        edgeEnd: str = "",
        json: dict = None,
        permissions: [str] = None,
        patchData: BaseData = None,
        returnData: BaseData = None,
    ) -> Response:
        edge = self.edgeMid + edgeEnd
        response = self.baseAPI.__patchAPI__(
            edgeEnd=edge,
            json=json,
            permissions=permissions,
            patchData=patchData,
            returnData=returnData,
        )
        return response

    def __deleteAPI__(
        self, edgeEnd: str = "", permissions: [str] = None, deleteData: BaseData = None
    ):
        edge = self.edgeMid + edgeEnd
        response = self.baseAPI.__deleteAPI__(
            edgeEnd=edge, permissions=permissions, deleteData=deleteData
        )
        return response
