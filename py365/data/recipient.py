# https://docs.microsoft.com/en-us/graph/api/resources/recipient
import attr
from .base_data import BaseData
from .email_address import EmailAddress


@attr.s(auto_attribs=True)
class Recipient(BaseData):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/recipient
    """

    emailAddress: EmailAddress = None
