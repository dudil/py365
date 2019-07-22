import logging
import requests
from typing import Optional
from urllib import parse

AUTHORITY_BASE_URL = "https://login.microsoftonline.com/"


class AppConnection(object):

    def __init__(self, app_id, app_secret, tenant_id, resource, api_ver):
        self.app_id = app_id
        self.app_secret = app_secret
        self.tenant_id = tenant_id
        self.resource = resource
        self.authority = f'{AUTHORITY_BASE_URL}{tenant_id}'
        self.api_base_url = f'{self.resource}/{api_ver}/'

    def verifyPermissions(self, permissions: [str]):
        # TODO: check we indeed have the required permissions
        pass

    # TODO: Move to Utils Package
    def get_api_url(self, endpoint: str):
        """Convert a relative path such as /me/photo/$value to a full URI
        This is much easier to work with how MS are actually documenting their API
        """
        if parse.urlparse(endpoint).scheme in ['http', 'https']:
            return endpoint  # url is already complete
        return parse.urljoin(self.api_base_url, endpoint.lstrip('/'))

    def getAccessToken(self) -> Optional[str]:
        raise NotImplementedError("pure function")

    def getSession(self) -> Optional[requests.Session]:
        accessToken = self.getAccessToken()
        if accessToken:
            session: requests.Session = requests.Session()
            session.headers.update({'Authorization': f'Bearer {accessToken}',
                                    'Content-type': 'application/json'})
            return session
        else:
            logging.error("no access token received")
            return None

    def get(self, endpoint: str, params: dict, permissions: [str] = None) -> requests.Response:
        self.verifyPermissions(permissions)
        url = self.get_api_url(endpoint)
        session = self.getSession()

        response = session.get(url, params=params)
        return response

    def post(self, endpoint: str, json: dict, permissions: [str] = None) -> requests.Response:
        self.verifyPermissions(permissions)
        url = self.get_api_url(endpoint)
        session = self.getSession()

        response = session.post(url, json=json)
        return response

    def patch(self, endpoint: str, json: dict, permissions: [str] = None) -> requests.Response:
        self.verifyPermissions(permissions)
        url = self.get_api_url(endpoint)
        session = self.getSession()

        response = session.patch(url, json=json)
        return response
