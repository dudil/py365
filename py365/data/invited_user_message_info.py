from pydantic import BaseModel


from .recipient import Recipient


class InvitedUserMessageInfo(BaseModel):
    """
    # https://docs.microsoft.com/en-us/graph/api/resources/invitedusermessageinfo
    """

    ccRecipient: Recipient = None
    customizedMessageBody: str = None
    messageLanguage: str = "en-US"
