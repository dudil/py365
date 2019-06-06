from py365 import auth, resources


class Graph365:
    """
    Graph365 represent the main entry point for the py365 package
    Use it in order to access all other elements in the package
    """

    def __init__(self, appId: str, appSecret: str, tenantId: str):
        self.appId = appId
        self.appSecret = appSecret
        self.tenantId = tenantId

        connection = auth.AppConnection(
            app_id=appId, app_secret=appSecret, tenant_id=tenantId)
        self.connection = connection

        self.users = resources.Users(connection=connection)
        self.invitations = resources.InvitationManager(connection=connection)
        self.planner = resources.Planner(connection=connection)
