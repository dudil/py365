# https://docs.microsoft.com/en-us/graph/api/resources/recipient
from pydantic import BaseModel

from .email_address import EmailAddress


class Recipient(BaseModel):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/recipient
    """

    emailAddress: EmailAddress = None
