from .base_data import BaseData
from .recipient import Recipient


class InvitedUserMessageInfo(BaseData):
    """
    # https://docs.microsoft.com/en-us/graph/api/resources/invitedusermessageinfo
    """

    ccRecipient: Recipient = None
    customizedMessageBody: str = None
    messageLanguage: str = "en-US"
