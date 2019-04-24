

# https://docs.microsoft.com/en-us/graph/api/resources/recipient
from resources.base_resource import BaseResource
from resources.email_address import EmailAddress


class Recipient(BaseResource):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/recipient
    """

    def __init__( self, emailAddress: EmailAddress ):
        self.emailAddress: EmailAddress = emailAddress
        BaseResource.__init__(self)
