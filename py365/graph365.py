from py365 import auth, resources, enums


class Graph365:
    """
    Graph365 represent the main entry point for the py365 package
    Use it in order to access all other elements in the package
    """

    def __init__(self, appId: str, tenantId: str
                 , connectionType: enums.ConnectionTypes = enums.ConnectionTypes.MSAL
                 , appSecret: str = None, username: str = None, password: str = None):
        self.appId = appId
        self.appSecret = appSecret
        self.tenantId = tenantId

        # not elegant but should work for now
        # TODO: Reformat
        if connectionType is enums.ConnectionTypes.MSAL:
            connection = auth.MsalConnection(
                app_id=appId, app_secret=appSecret, tenant_id=tenantId
                , username=username, password=password)
        else:
            connection = auth.AdalConnection(
                app_id=appId, app_secret=appSecret, tenant_id=tenantId)

        self.connection = connection

        self.users = resources.Users(connection=connection)
        self.invitations = resources.InvitationManager(connection=connection)
        self.planner = resources.Planner(connection=connection)
        self.groups = resources.Groups(connection=connection)
