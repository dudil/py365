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

class InvitationManager:
    # Class Private Consts
    __CREATE_INVITATION_ENDPOINT = '/invitations'

    # Initialisation method
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

    # API Reference:
    # https://docs.microsoft.com/en-us/graph/api/invitation-post
    def createInvitation(self):
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
        
        response = self.connection.post(
            self.__CREATE_INVITATION_ENDPOINT, json=payload)
        #TODO check for valid reponse
        self.redeem_url = response.json().get("inviteRedeemUrl", None)
        self.status = response.json().get("status", InvitationStatuValues.ERROR)
        self.invited_user = response.json().get("invitedUser", None)

