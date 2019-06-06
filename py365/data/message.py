import attr

from ._base_data import BaseData
from .item_body import ItemBody
from .recipient import Recipient


@attr.s(auto_attribs=True)
class BaseMessage(BaseData):
    subject: str = None
    body: ItemBody = None
    toRecipients: [Recipient] = None
    ccRecipients: [Recipient] = None
