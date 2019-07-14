import logging
from typing import Optional
from msal import ConfidentialClientApplication
from .app_connection import AppConnection

DEFAULT_API_VER = "v1.0"
DEFAULT_RESOURCE = "https://graph.microsoft.com/"
DEFAULT_SCOPES = ["https://graph.microsoft.com/.default"]


class MsalConnection(AppConnection):
    """ Implementation of the Connection class using msal """

    def __init__(self, app_id, app_secret, tenant_id, resource=DEFAULT_RESOURCE, api_ver=DEFAULT_API_VER):
        super().__init__(app_id=app_id, app_secret=app_secret
                         , tenant_id=tenant_id, resource=resource, api_ver=api_ver)
        self.scopes = DEFAULT_SCOPES
        self.app = None

    def getAccessToken(self) -> Optional[str]:
        # Initialise the app if not already exist
        if not self.app:
            logging.info("Initialise msal connection app")
            self.app = ConfidentialClientApplication(client_id=self.app_id, authority=self.authority
                                                     , client_credential=self.app_secret)
        # try to get the token from cache if already exist
        result = self.app.acquire_token_silent(scopes=self.scopes, account=None)
        if not result:
            logging.info("No suitable token exists in cache. Let's get a new one from AAD.")
            result = self.app.acquire_token_for_client(scopes=self.scopes)

        if "access_token" in result:
            return result["access_token"]

        return None
