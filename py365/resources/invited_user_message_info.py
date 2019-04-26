from ._base_resource import BaseResource
from .recipient import Recipient


class InvitedUserMessageInfo(BaseResource):
    """
    # https://docs.microsoft.com/en-us/graph/api/resources/invitedusermessageinfo
    """

    def __init__( self,
                  ccRecipient: Recipient,
                  customizedMessageBody: str,
                  messageLanguage: str = "en-US" ):
        self.ccRecipient: Recipient = ccRecipient
        self.customizedMessageBody: str = customizedMessageBody
        self.messageLanguage: str = messageLanguage
        BaseResource.__init__(self)
