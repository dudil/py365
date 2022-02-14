"""
Represent the email address OG resource
"""
from py365.utils import OptStr
from .base_data import BaseData


class EmailAddress(BaseData):
    address: OptStr = None
    name: OptStr = None
