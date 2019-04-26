from enum import Enum


class InvitationStatusValues(Enum):
    """
    Enum to represent the different invitation status
    """
    PENDING = "PendingAcceptance"
    COMPLETED = "Completed"
    IN_PROGRESS = "InProgress"
    ERROR = "Error"
