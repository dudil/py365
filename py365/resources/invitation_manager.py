# API Reference:
# https://docs.microsoft.com/en-us/graph/api/resources/invitation


from py365.auth import AppConnection
from py365.data import Invitation
from py365.enums import InvitationStatusValues


class InvitationManager(object):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/invitation
    """

    def __init__(self, connection: AppConnection):
        self.__CREATE_INVITATION_ENDPOINT = '/invitations'
        self.connection = connection

    def createInvitation(self, invitation: Invitation) -> Invitation:
        """
        https://docs.microsoft.com/en-us/graph/api/invitation-post
        :param invitation:
        :type invitation:
        :return:
        :rtype:
        """
        response = self.connection.post(
            self.__CREATE_INVITATION_ENDPOINT, json=invitation.json)
        # TODO check for valid response
        invitation.inviteRedeemUrl = response.json().get("inviteRedeemUrl", None)
        invitation.status = response.json().get("status", InvitationStatusValues.ERROR)
        invitation.invitedUser = response.json().get("invitedUser", None)

        return invitation
