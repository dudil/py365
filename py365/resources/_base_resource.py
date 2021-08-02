import urllib.parse
from requests import Response
from py365.auth import AppConnection
from py365.data import BaseData


class BaseResource:
    """
    Represent a base resource API on the OG
    Every OG API class should inherit from this class
    """

    def __init__(self, connection: AppConnection, edgeBase):
        self._connection: AppConnection = connection
        self.EDGE_BASE = edgeBase

    @staticmethod
    def __getResponseData__(data: BaseData, response: Response):
        if data and response.ok:
            if response.text:
                respJson = response.json()
                data.fromResponse(data=respJson)
            if "ETag" in response.headers:
                data.eTag = response.headers["ETag"]

    def __getAPI__(
        self,
        edgeEnd: str = "",
        params: dict = None,
        permissions: [str] = None,
        returnData: BaseData = None,
    ) -> Response:
        endpoint = self.EDGE_BASE + edgeEnd
        endpoint = urllib.parse.quote(endpoint)
        response = self._connection.get(
            endpoint=endpoint, params=params, permissions=permissions
        )
        self.__getResponseData__(returnData, response)
        return response

    def __postAPI__(
        self,
        edgeEnd: str = "",
        json: dict = None,
        permissions: [str] = None,
        postData: BaseData = None,
        returnData: BaseData = None,
    ) -> Response:
        endpoint = self.EDGE_BASE + edgeEnd
        endpoint = urllib.parse.quote(endpoint)
        addHeaders = {}
        if postData:
            json = postData.json
            if postData.eTag:
                addHeaders.update({"If-Match": postData.eTag})
        response = self._connection.post(
            endpoint=endpoint, json=json, permissions=permissions, addHeaders=addHeaders
        )
        self.__getResponseData__(returnData, response)
        return response

    def __patchAPI__(
        self,
        edgeEnd: str = "",
        json: dict = None,
        permissions: [str] = None,
        patchData: BaseData = None,
        returnData: BaseData = None,
    ) -> Response:
        endpoint = self.EDGE_BASE + edgeEnd
        endpoint = urllib.parse.quote(endpoint)
        addHeaders = {}
        if patchData:
            json = patchData.json
            if patchData.eTag:
                addHeaders.update({"If-Match": patchData.eTag})
        response = self._connection.patch(
            endpoint=endpoint, json=json, permissions=permissions, addHeaders=addHeaders
        )
        self.__getResponseData__(returnData, response)
        return response

    def __deleteAPI__(
        self, edgeEnd: str = "", permissions: [str] = None, deleteData: BaseData = None
    ):
        endpoint = self.EDGE_BASE + edgeEnd
        endpoint = urllib.parse.quote(endpoint)
        addHeaders = {}
        if deleteData:
            if deleteData.eTag:
                addHeaders.update({"If-Match": deleteData.eTag})
        response = self._connection.delete(
            endpoint=endpoint, permissions=permissions, addHeaders=addHeaders
        )
        return response
