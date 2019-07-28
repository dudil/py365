"""
Represent the email address OG resource
"""
import attr
from .base_data import BaseData


@attr.s(auto_attribs=True)
class EmailAddress(BaseData):
    address: str = None
    name: str = None
