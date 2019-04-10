from . import AppConnection
from . import Users
from . import InvitationManager

class Py365:
    def __init__(self, appId: str, appSecret: str, tenantId: str):
        self.appId = appId
        self.appSecret = appSecret
        self.tenantId = tenantId

        connection = AppConnection(
            app_id=appId, app_secret=appSecret, tenant_id=tenantId)
        self.connection = connection

        self.users = Users(connection=connection)
        self.invitations = InvitationManager(connection=connection)
