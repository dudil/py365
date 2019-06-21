from py365 import auth


class BaseResource:
    """
    Represent a base resource on the OG
    Every OG data class should inherit from this class
    """

    def __init__(self, connection: auth.AppConnection, endpoint):
        self.connection: auth.AppConnection = connection
        self.ENDPOINT = endpoint
