# API Reference:
# https://docs.microsoft.com/en-us/graph/api/resources/invitation

from enum import Enum
from dataclasses import dataclass

from .. import AppConnection
from .. import Recipient
from .. import utils

class InvitedUserTypes(Enum):
    GUEST = "Guest"
    MEMBER = "Member"

class InvitationStatuValues(Enum):
    PENDING = "PendingAcceptance"
    COMPLETED = "Completed"
    IN_PROGRESS = "InProgress"
    ERROR = "Error"

# https://docs.microsoft.com/en-us/graph/api/resources/invitedusermessageinfo
@dataclass
class InvitedUserMessageInfo:
    ccRecipient: Recipient
    customizedMessageBody : str
    messageLanguage: str = "en-US"

    def __repr__(self):
        repr = {
            "ccRecipients": [ccRecipient],
            "customizedMessageBody": customizedMessageBody,
            "messageLanguage": messageLanguage
        }
        return repr
@dataclass
class Invitation:
    display_name: str
    email: str
    send_message: bool = True
    user_type: InvitedUserTypes = InvitedUserTypes.GUEST
    redirect_url: str = "https://office.com"
    redeem_url: str = None
    _status: InvitationStatuValues = None
    _invited_user = None
    message = None

    def toPayload(self):
        payload = {}
        
        payload = utils.addPayloadParam(
            payload, "invitedUserEmailAddress", self.email)
        payload = utils.addPayloadParam(
            payload, "inviteRedirectUrl", self.redirect_url)
        payload = utils.addPayloadParam(
            payload, "invitedUserDisplayName", self.display_name)
        payload = utils.addPayloadParam(
            payload, "invitedUserType", self.user_type.value)
        payload = utils.addPayloadParam(
            payload, "sendInvitationMessage", self.send_message)
        payload = utils.addPayloadParam(
            payload, "invitedUserMessageInfo", self.message)

        return payload
    
    @property
    def invited_user(self):
        return self._invited_user.get("id", None)


class InvitationManager:
    # Initialisation method
    def __init__(self, connection: AppConnection):
        self.__CREATE_INVITATION_ENDPOINT = '/invitations'
        self.connection = connection

    # API Reference:
    # https://docs.microsoft.com/en-us/graph/api/invitation-post
    def createInvitation(self, invitation:Invitation):
        
        response = self.connection.post(
            self.__CREATE_INVITATION_ENDPOINT, json=invitation.toPayload())
        #TODO check for valid reponse
        invitation.redeem_url = response.json().get("inviteRedeemUrl", None)
        invitation._status = response.json().get("status", InvitationStatuValues.ERROR)
        invitation._invited_user = response.json().get("invitedUser", None)

        return invitation

