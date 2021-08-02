"""
Represent the email address OG resource
"""
from pydantic import BaseModel
from py365.utils import OptStr


class EmailAddress(BaseModel):
    address: OptStr = None
    name: OptStr = None
