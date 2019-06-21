"""
https://docs.microsoft.com/en-us/graph/api/resources/identityset
"""

from ._base_data import BaseData
from .identity import Identity
import attr


@attr.s(auto_attribs=True)
class IdentitySet(BaseData):
    """
    The IdentitySet resource is a keyed collection of identity resources.
    It is used to represent a set of identities associated with various events for an item,
    such as created by or last modified by.
    """

    application: Identity = None
    device: Identity = None
    user: Identity = None
