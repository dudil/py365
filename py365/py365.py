from py365.apis import InvitationManager, Users
from py365.auth import AppConnection


class Py365:
    """
    Py365 represent the main entry point for the py365 package
    Use it in order to access all other elements in the package
    """

    def __init__(self, appId: str, appSecret: str, tenantId: str):
        self.appId = appId
        self.appSecret = appSecret
        self.tenantId = tenantId

        connection = AppConnection(
            app_id=appId, app_secret=appSecret, tenant_id=tenantId)
        self.connection = connection

        self.users = Users(connection=connection)
        self.invitations = InvitationManager(connection=connection)
