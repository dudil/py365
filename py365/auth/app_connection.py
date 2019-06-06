import urllib

import requests
from adal import AuthenticationContext

DEFAULT_API_VER = "v1.0"
DEFAULT_RESOURCE = "https://graph.microsoft.com/"
AUTHORITY_BASE_URL = "https://login.microsoftonline.com/"


class AppConnection(object):
    """ Implementation of the Connection class using adal instead of OAuth """

    def __init__(self, app_id, app_secret, tenant_id, resource=DEFAULT_RESOURCE, api_ver=DEFAULT_API_VER):
        # TODO parameter verification!!!
        self.app_id = app_id
        self.app_secret = app_secret
        self.resource = resource
        self.authority = f'{AUTHORITY_BASE_URL}{tenant_id}'
        self.api_base_url = f'{self.resource}/{api_ver}/'
        self.session: requests.Session = None

    def verifyPermissions(self, permissions: [str]):
        # TODO: check we indeed have the required permissions
        pass

    # TODO: Move to Utils Package
    def get_api_url(self, endpoint: str):
        """Convert a relative path such as /me/photo/$value to a full URI
        This is much easier to work with how MS are actually documenting their API
        """
        if urllib.parse.urlparse(endpoint).scheme in ['http', 'https']:
            return endpoint  # url is already complete
        return urllib.parse.urljoin(self.api_base_url, endpoint.lstrip('/'))

    def authenticate(self):
        context = AuthenticationContext(self.authority)
        token = context.acquire_token_with_client_credentials(self.resource, self.app_id, self.app_secret)
        self.session: requests.Session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {token["accessToken"]}',
                                     'Content-type': 'application/json'})

    def get(self, endpoint: str, params=None, permissions: [str] = None):
        self.verifyPermissions(permissions)
        url = self.get_api_url(endpoint)
        if self.session is None:
            self.authenticate()

        response = self.session.get(url, params=params)
        return response

    def post(self, endpoint: str, json: dict = None, permissions: [str] = None):
        self.verifyPermissions(permissions)
        url = self.get_api_url(endpoint)
        if self.session is None:
            self.authenticate()

        response = self.session.post(url, json=json)
        return response

    def patch(self, endpoint: str, json: dict, permissions: [str] = None):
        self.verifyPermissions(permissions)
        url = self.get_api_url(endpoint)
        if self.session is None:
            self.authenticate()

        response = self.session.patch(url, json=json)
        return response
