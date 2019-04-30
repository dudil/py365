from py365.enums import InvitationStatusValues, InvitedUserTypes
from ._base_resource import BaseResource


class Invitation(BaseResource):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/invitation
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
        self._status: InvitationStatusValues = InvitationStatusValues.ERROR
        self._invited_user = None
        BaseResource.__init__(self)

    @property
    def invited_user( self ):
        """

        :return: get the invited user id
        :rtype:
        """
        return self._invited_user.get("id", None)
