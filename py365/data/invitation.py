import attr

from py365.enums import InvitationStatusValues, UserTypes

from .base_data import BaseData
from .user import User


@attr.s(auto_attribs=True)
class Invitation(BaseData):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/invitation
    """
    invitedUserDisplayName: str = None
    invitedUserEmailAddress: str = None
    inviteRedeemUrl: str = None
    invitedUser: User = None
    status: InvitationStatusValues = InvitationStatusValues.ERROR
    sendInvitationMessage: bool = True
    invitedUserType: UserTypes = UserTypes.GUEST
    inviteRedirectUrl: str = "https://office.com"
    # invitedUserMessageInfo : InvitedUserMessageInfo
