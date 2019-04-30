"""
Represent the email address OG resource
"""
from ._base_resource import BaseResource


class EmailAddress(BaseResource):
    """
    Class to represent an EmailAddress OG resource
    :param address: the email address (req)
    :type address: str
    :param name: the name of the email owner (req)
    :type name: str
    """

    def __init__( self, address: str, name: str ):
        BaseResource.__init__(self)
        self.address: str = address
        self.name: str = name
