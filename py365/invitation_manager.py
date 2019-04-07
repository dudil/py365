from enum import Enum
from .app_connection import AppConnection

INVITATION_ENDPOINT = '/invitations'


class InvitedUserTypes(Enum):
    GUEST = "Guest"
    MEMBER = "Member"

class InvitationStatuValues(Enum):
    PENDING = "PendingAcceptance"
    COMPLETED = "Completed"
    IN_PROGRESS = "InProgress"
    ERROR = "Error"


class InvitationManager:

    def __init__(self, connection: AppConnection, email: str, 
        redirect_url: str, display_name: str = None, 
        send_message: bool = False, user_type: InvitedUserTypes = InvitedUserTypes.GUEST):

        self.connection = connection
        self.display_name: str = display_name
        self.email: str = email
        self.message = None
        self.redirect_url: str = redirect_url
        self.send_message: bool = send_message
        self.redeem_url: str = None
        self.user_type: InvitedUserTypes = user_type
        self.status: InvitationStatuValues = None
        self.invited_user = None


    def __addPayloadParam__(self, payload: dict, key: str, value: any):
        payload.update({key: value} if value else {})
        return payload


    def CreateInvitation(self):
        payload = {}
        payload = self.__addPayloadParam__(
            payload, "invitedUserEmailAddress", self.email)
        payload = self.__addPayloadParam__(
            payload, "inviteRedirectUrl", self.redirect_url)
        payload = self.__addPayloadParam__(
            payload, "invitedUserDisplayName", self.display_name)
        payload = self.__addPayloadParam__(
            payload, "invitedUserType", self.user_type.value)
        payload = self.__addPayloadParam__(
            payload, "sendInvitationMessage", self.send_message)
        payload = self.__addPayloadParam__(
            payload, "invitedUserMessageInfo", self.message)
        
        response = self.connection.post(INVITATION_ENDPOINT, json=payload)
        #TODO check for valid reponse
        self.redeem_url = response.json().get("inviteRedeemUrl", None)
        self.status = response.json().get("status", InvitationStatuValues.ERROR)
        self.invited_user = response.json().get("invitedUser", None)


#### Create invitation
