from ._base_resource import BaseResource
from .item_body import ItemBody
from .recipient import Recipient


class BaseMessage(BaseResource):

    def __init__(self, subject: str
                 , body: ItemBody
                 , toRecipients: [Recipient]
                 , ccRecipients: [Recipient] = None):
        self.subject = subject
        self.body = body
        self.toRecipients = toRecipients
        self.ccRecipients = ccRecipients
        BaseResource.__init__(self)
