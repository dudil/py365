from adal import AuthenticationContext
from typing import Optional
from .app_connection import AppConnection

DEFAULT_API_VER = "v1.0"
DEFAULT_RESOURCE = "https://graph.microsoft.com/"


class AdalConnection(AppConnection):
    """ Implementation of the Connection class using adal instead of OAuth """

    def __init__(
        self,
        app_id,
        app_secret,
        tenant_id,
        resource=DEFAULT_RESOURCE,
        api_ver=DEFAULT_API_VER,
    ):
        super().__init__(
            app_id=app_id,
            app_secret=app_secret,
            tenant_id=tenant_id,
            resource=resource,
            api_ver=api_ver,
        )

    def getAccessToken(self) -> Optional[str]:
        context = AuthenticationContext(self.authority)
        token = context.acquire_token_with_client_credentials(
            self.resource, self.app_id, self.app_secret
        )
        if token and "access_token" in token:
            return token["accessToken"]

        return None
