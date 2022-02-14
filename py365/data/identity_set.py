"""
https://docs.microsoft.com/en-us/graph/api/resources/identityset
"""

from typing import Optional

from .base_data import BaseData
from .identity import Identity


class IdentitySet(BaseData):
    """
    The IdentitySet resource is a keyed collection of identity resources.
    It is used to represent a set of identities associated with various events for an item,
    such as created by or last modified by.
    """

    application: Optional[Identity] = None
    device: Optional[Identity] = None
    user: Optional[Identity] = None
