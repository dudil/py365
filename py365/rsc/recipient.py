

# https://docs.microsoft.com/en-us/graph/api/resources/recipient
from ._base_resource import BaseResource
from .email_address import EmailAddress


class Recipient(BaseResource):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/recipient
    """

    def __init__( self, emailAddress: EmailAddress ):
        self.emailAddress: EmailAddress = emailAddress
        BaseResource.__init__(self)
