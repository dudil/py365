from typing import Optional
from pydantic import BaseModel

from py365.enums import InvitationStatusValues, UserTypes
from py365.utils import OptStr

from .user import User


class Invitation(BaseModel):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/invitation
    """

    invitedUserDisplayName: OptStr = None
    invitedUserEmailAddress: OptStr = None
    inviteRedeemUrl: OptStr = None
    invitedUser: Optional[User] = None
    status: InvitationStatusValues = InvitationStatusValues.ERROR
    sendInvitationMessage: bool = True
    invitedUserType: UserTypes = UserTypes.GUEST
    inviteRedirectUrl: str = "https://office.com"
    # invitedUserMessageInfo : InvitedUserMessageInfo
