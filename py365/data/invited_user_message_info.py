import attr

from ._base_data import BaseData
from .recipient import Recipient


@attr.s(auto_attribs=True)
class InvitedUserMessageInfo(BaseData):
    """
    # https://docs.microsoft.com/en-us/graph/api/resources/invitedusermessageinfo
    """

    ccRecipient: Recipient = None
    customizedMessageBody: str = None
    messageLanguage: str = "en-US"
