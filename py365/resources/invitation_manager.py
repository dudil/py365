# API Reference:
# https://docs.microsoft.com/en-us/graph/api/resources/invitation

from ._base_resource import BaseResource
from py365.auth import AppConnection
from py365.data import Invitation
from py365.enums import InvitationStatusValues


class InvitationManager(BaseResource):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/invitation
    """

    def __init__(self, connection: AppConnection):
        super().__init__(connection=connection, edgeBase="/invitations")

    def createInvitation(self, invitation: Invitation) -> Invitation:
        """
        https://docs.microsoft.com/en-us/graph/api/invitation-post
        :param invitation:
        :type invitation:
        :return:
        :rtype:
        """
        response = self.__postAPI__(json=invitation.json)
        # TODO check for valid response
        invitation.inviteRedeemUrl = response.json().get("inviteRedeemUrl", None)
        invitation.status = response.json().get("status", InvitationStatusValues.ERROR)
        invitation.invitedUser = response.json().get("invitedUser", None)

        return invitation
