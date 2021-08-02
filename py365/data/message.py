from pydantic import BaseModel


from .item_body import ItemBody
from .recipient import Recipient


class BaseMessage(BaseModel):
    subject: str = None
    body: ItemBody = None
    toRecipients: [Recipient] = None
    ccRecipients: [Recipient] = None
