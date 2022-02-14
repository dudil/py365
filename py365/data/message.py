from .base_data import BaseData

from .item_body import ItemBody
from .recipient import Recipient


class BaseMessage(BaseData):
    subject: str = None
    body: ItemBody = None
    toRecipients: [Recipient] = None
    ccRecipients: [Recipient] = None
