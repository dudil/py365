from enum import Enum


class UserTypes(Enum):
    """
    Enum to represent rhw different user types we can invite
    """

    GUEST = "Guest"
    MEMBER = "Member"
