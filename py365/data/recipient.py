# https://docs.microsoft.com/en-us/graph/api/resources/recipient

from .base_data import BaseData
from .email_address import EmailAddress


class Recipient(BaseData):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/recipient
    """

    emailAddress: EmailAddress = None
