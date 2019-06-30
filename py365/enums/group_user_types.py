from enum import Enum


class GroupUserTypes(Enum):
    """
    Enum to represent the different users we have in groups
    """
    MEMBER = "Member"
    OWNER = "Owner"
