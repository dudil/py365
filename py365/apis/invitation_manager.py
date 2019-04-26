# API Reference:
# https://docs.microsoft.com/en-us/graph/api/resources/invitation


from py365.auth import AppConnection
from py365.enums import InvitationStatusValues
from py365.resources import Invitation


class InvitationManager(object):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/invitation
    """

    def __init__( self, connection: AppConnection ):
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
            self.__CREATE_INVITATION_ENDPOINT, json=invitation.payload)
        # TODO check for valid response
        invitation.redeem_url = response.json().get("inviteRedeemUrl", None)
        invitation._status = response.json().get("status", InvitationStatusValues.ERROR)
        invitation._invited_user = response.json().get("invitedUser", None)

        return invitation
