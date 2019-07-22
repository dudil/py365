import requests
import urllib.parse
from py365 import auth


class BaseResource:
    """
    Represent a base resource API on the OG
    Every OG API class should inherit from this class
    """

    def __init__(self, connection: auth.AppConnection, edgeBase):
        self._connection: auth.AppConnection = connection
        self.EDGE_BASE = edgeBase

    def getAPI(self, edgeEnd: str = "", params: dict = None, permissions: [str] = None) -> requests.Response:
        endpoint = self.EDGE_BASE + edgeEnd
        endpoint = urllib.parse.quote(endpoint)
        response = self._connection.get(endpoint=endpoint, params=params, permissions=permissions)

        return response

    def postAPI(self, edgeEnd: str = "", json: dict = None, permissions: [str] = None) -> requests.Response:
        endpoint = self.EDGE_BASE + edgeEnd
        endpoint = urllib.parse.quote(endpoint)
        response = self._connection.post(endpoint=endpoint, json=json, permissions=permissions)

        return response

    def patchAPI(self, edgeEnd: str = "", json: dict = None, permissions: [str] = None) -> requests.Response:
        endpoint = self.EDGE_BASE + edgeEnd
        endpoint = urllib.parse.quote(endpoint)
        response = self._connection.patch(endpoint=endpoint, json=json, permissions=permissions)

        return response
