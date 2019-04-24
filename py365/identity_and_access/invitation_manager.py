# API Reference:
# https://docs.microsoft.com/en-us/graph/api/resources/invitation

from enum import Enum

from core.app_connection import AppConnection
from resources.base_resource import BaseResource
from resources.recipient import Recipient


class InvitedUserTypes(Enum):
    """
    Enum to represent rhw different user types we can invite
    """
    GUEST = "Guest"
    MEMBER = "Member"


class InvitationStatusValues(Enum):
    """
    Enum to represent the different invitation status
    """
    PENDING = "PendingAcceptance"
    COMPLETED = "Completed"
    IN_PROGRESS = "InProgress"
    ERROR = "Error"


class InvitedUserMessageInfo(BaseResource):
    """
    # https://docs.microsoft.com/en-us/graph/api/resources/invitedusermessageinfo
    """

    def __init__( self,
                  ccRecipient: Recipient,
                  customizedMessageBody: str,
                  messageLanguage: str = "en-US" ):
        self.ccRecipient: Recipient = ccRecipient
        self.customizedMessageBody: str = customizedMessageBody
        self.messageLanguage: str = messageLanguage
        BaseResource.__init__(self)


class Invitation(BaseResource):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/invitation?
    """

    def __init__( self,
                  display_name: str,
                  email: str,
                  send_message: bool = True,
                  user_type: InvitedUserTypes = InvitedUserTypes.GUEST,
                  redirect_url: str = "https://office.com",
                  redeem_url: str = None,
                  message=None ):
        self.display_name: str = display_name
        self.email: str = email
        self.send_message: bool = send_message
        self.user_type: InvitedUserTypes = user_type
        self.redirect_url: str = redirect_url
        self.redeem_url: str = redeem_url
        self.message = message
        self._status: InvitationStatusValues = None
        self._invited_user = None
        BaseResource.__init__(self)


    @property
    def invited_user(self):
        """

        :return: get the invited user id
        :rtype:
        """
        return self._invited_user.get("id", None)


class InvitationManager(object):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/invitation
    """
    def __init__(self, connection: AppConnection):
        self.__CREATE_INVITATION_ENDPOINT = '/invitations'
        self.connection = connection

    def createInvitation( self, invitation: Invitation ):
        """
        https://docs.microsoft.com/en-us/graph/api/invitation-post
        :param invitation:
        :type invitation:
        :return:
        :rtype:
        """
        response = self.connection.post(
            self.__CREATE_INVITATION_ENDPOINT, json=invitation.payload())
        # TODO check for valid response
        invitation.redeem_url = response.json().get("inviteRedeemUrl", None)
        invitation._status = response.json().get("status", InvitationStatusValues.ERROR)
        invitation._invited_user = response.json().get("invitedUser", None)

        return invitation
