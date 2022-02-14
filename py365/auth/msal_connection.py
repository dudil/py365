import logging
from typing import Optional

import httpx
from msal import ConfidentialClientApplication, PublicClientApplication

from .app_connection import AppConnection, CallMethod, GraphResponse

AUTHORITY_BASE_URL = "https://login.microsoftonline.com/"
DEFAULT_API_VER = "v1.0"
DEFAULT_RESOURCE = "https://graph.microsoft.com/"
DEFAULT_SCOPES = ["https://graph.microsoft.com/.default"]


class MsalConnection(AppConnection):
    """Implementation of the Connection class using msal"""

    def __init__(
        self,
        app_id: str,
        tenant_id: str,
        app_secret: str = None,
        username: str = None,
        password: str = None,
        resource: str = DEFAULT_RESOURCE,
        api_ver: str = DEFAULT_API_VER,
    ):
        super().__init__(
            resource=resource,
            api_ver=api_ver,
        )
        self.app_id = app_id
        self.app_secret = app_secret
        self.tenant_id = tenant_id
        self.username = username
        self.password = password
        self.authority = f"{AUTHORITY_BASE_URL}{tenant_id}"
        self.scopes = DEFAULT_SCOPES
        self.app = None

    def request_from_graph(
        self,
        method: CallMethod,
        url: str,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        headers: Optional[dict] = None,
    ) -> GraphResponse:
        request = httpx.Request(
            method=method.value, url=url, params=params, json=data, headers=headers
        )
        access_token = self.get_access_token()
        if not access_token:
            raise ConnectionError("No Access Token")

        request.headers.update(
            {
                "Authorization": f"Bearer {access_token}",
                "Content-type": "application/data",
            }
        )

        with httpx.Client() as client:
            response = client.send(request=request)
            graph_response = GraphResponse(
                status_code=response.status_code,
                headers=response.headers,
                content=response.content,
                json=response.json(),
                text=response.text,
            )
        return graph_response

    def get_access_token(self) -> Optional[str]:
        if self.app_secret:
            return self.get_confidential_client_access_token()

        return self.get_public_access_token()

    def get_confidential_client_access_token(self) -> Optional[str]:
        # Initialise the app if not already exist
        if not self.app:
            logging.info("Initialise msal connection app")
            self.app = ConfidentialClientApplication(
                client_id=self.app_id,
                authority=self.authority,
                client_credential=self.app_secret,
            )
        # try to get the token from cache if already exist
        result = self.app.acquire_token_silent(scopes=self.scopes, account=None)
        if not result:
            logging.info(
                "No suitable token exists in cache. Let's get a new one from AAD."
            )
            result = self.app.acquire_token_for_client(scopes=self.scopes)

        if "access_token" in result:
            return result["access_token"]
        return None

    def get_device_flow_access_token(self):
        if not self.app:
            # must have app initialised before calling that method
            print("App must be initialised before calling get_device_flow_access_token")
            return None

        flow = self.app.initiate_device_flow(scopes=self.scopes)
        print(flow["message"])
        print(flow["verification_uri"])
        print(flow["user_code"])
        return self.app.acquire_token_by_device_flow(flow)

    def get_username_password_access_token(self):
        if not self.app:
            # must have app initialised before calling that method
            print(
                "App must be initialised before calling get_username_password_access_token"
            )
            return None

        return self.app.acquire_token_by_username_password(
            self.username, self.password, scopes=self.scopes
        )

    def get_public_access_token(self) -> Optional[str]:
        # Initialise the app if not already exist
        if not self.app:
            print("Initialise msal connection app")
            self.app = PublicClientApplication(
                client_id=self.app_id, authority=self.authority
            )

        result = None
        accounts = self.app.get_accounts()
        if accounts:
            # TODO: need to pick the relevant account to proceed
            chosen = accounts[0]

            # try to get the token from cache if already exist
            result = self.app.acquire_token_silent(scopes=self.scopes, account=chosen)

        if not result:
            print("No suitable token exists in cache. Let's get a new one from AAD.")
            if self.username and self.password:
                result = self.get_username_password_access_token()
            else:
                result = self.get_device_flow_access_token()

        if "access_token" in result:
            return result["access_token"]
        return None
