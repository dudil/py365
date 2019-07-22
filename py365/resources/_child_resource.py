import requests

from ._base_resource import BaseResource


class ChildResource:
    """
    Represent a child resource on the OG
    Every OG API class that represent a child API should inherit from this class
    """

    def __init__(self, baseAPI: BaseResource, edgeMid: str):
        self.baseAPI: BaseResource = baseAPI
        self.edgeMid = edgeMid

    def getAPI(self, edgeEnd: str = "", params: dict = None, permissions: [str] = None) -> requests.Response:
        edge = self.edgeMid + edgeEnd
        response = self.baseAPI.getAPI(edgeEnd=edge, params=params, permissions=permissions)
        return response

    def postAPI(self, edgeEnd: str = "", json: dict = None, permissions: [str] = None) -> requests.Response:
        edge = self.edgeMid + edgeEnd
        response = self.baseAPI.postAPI(edgeEnd=edge, json=json, permissions=permissions)
        return response

    def patchAPI(self, edgeEnd: str = "", json: dict = None, permissions: [str] = None) -> requests.Response:
        edge = self.edgeMid + edgeEnd
        response = self.baseAPI.patchAPI(edgeEnd=edge, json=json, permissions=permissions)
        return response
