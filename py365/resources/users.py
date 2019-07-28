"""
https://docs.microsoft.com/en-us/graph/api/resources/users
"""
from typing import Optional
from py365 import auth, data
from ._base_resource import BaseResource
from ._child_resource import ChildResource


class Users(BaseResource):
    """
    You can use Microsoft Graph365 to build compelling app experiences based on users,
    their relationships with other users and groups, and their mail, calendar, and files.

    You can access users through Microsoft Graph365 in two ways:

    * By their ID, /users/{id | userPrincipalName}
    * By using the /me alias for the signed-in user, which is the same as /users/{signed-in user's id}
    """

    class User(ChildResource):
        """
        Class User is the user edge related to user operations
        """

        # user key can be either id or login mail
        def __init__(self, usersAPI: BaseResource, userKey: str):
            self.userKey = userKey
            super().__init__(baseAPI=usersAPI, edgeMid=f'/{userKey}')

        def getUser(self) -> data.User:
            """
            https://docs.microsoft.com/en-us/graph/api/user-get
            Retrieve the properties and relationships of user object.

            :return: the found user object
            :rtype: User
            """

            user: data.User = data.User()
            response = self.__getAPI__()
            if response.ok:
                respJson = response.json()
                user.fromResponse(respJson)
            else:
                print(f'Request Error{response.text}')
            return user

        def updateUser(self, userData: data.User):
            """
            https://docs.microsoft.com/en-us/graph/api/user-update
            Update the properties of a user object.

            :param userData:
            :type userData:
            :return:
            :rtype:
            """
            response = self.__patchAPI__(json=userData.json)

            if response.ok:
                print(f'updateUser Request OK!')
            else:
                print(f'updateUser Request Error{response.text}')

        def sendMail(self, message: data.BaseMessage, saveToSentItems: bool = True):
            """
            https://docs.microsoft.com/en-us/graph/api/user-sendmail?view=graph-rest-1.0
            send mail from the user inbox
            :param message: message to send
            :type message: BaseMessage Resource Class
            :param saveToSentItems: Indicates whether to save the message in Sent Items.
                                    Specify it only if the parameter is false; default is true. Optional.
            :type saveToSentItems: Boolean
            :return: call response
            :rtype: Response
            """
            payload = {
                "message": message.json,
                "saveToSentItems": saveToSentItems
            }
            response = self.__postAPI__(edgeEnd='/sendMail', json=payload)
            return response

        def getMemberGroups(self, securityEnabledOnly: bool = False) -> [str]:
            """
            https://docs.microsoft.com/en-us/graph/api/user-getmembergroups?view=graph-rest-1.0
            :return:
            :rtype:
            """

            payload = {
                "securityEnabledOnly": securityEnabledOnly
            }
            response = self.__postAPI__(edgeEnd='/getMemberGroups', json=payload)
            groups: [str] = []
            if response.ok:
                groups = response.json().get("value")
            else:
                print(f'Request Error {response.text}')
            return groups

    def __init__(self, connection: auth.AppConnection):
        """
        Initialisation method for the *Users* class
        :param connection: graph connection
        :type connection: AppConnection
        """
        BaseResource.__init__(self, connection=connection, edgeBase='/users/')

    def user(self, userKey: str) -> User:
        """
        This method represent a user API edge following the Users edge
        NB! Not to confuse with the data.User class which is critical to the graph operation.
        Why MS decided on that (kind of strange) flow, is not very clear to me.
        A better design would be probably to make the User API as major instead of Users/UserID
        Users, would match better a group of users where the default group is all.
        This would make it more meaningful and simple... Anyway....
        :param userKey: The user identification key; could be the user object tenant id or the principal name (login id)
        :type userKey: str
        :return: a User API object that will handle a specific user API operations
        :rtype: Users -> User subclass
        """
        userAPI = Users.User(usersAPI=self, userKey=userKey)
        return userAPI

    def createUser(self, newUser: data.User) -> Optional[data.User]:
        """
        https://docs.microsoft.com/en-us/graph/api/user-post-users
        Use this API to create a new User. The request body contains the user to create.
        At a minimum, you must specify the required properties for the user.
        You can optionally specify any other writable properties.
        :param newUser:
        :type newUser:
        :return:
        :rtype:
        """

        assert (newUser.accountEnabled is not None)
        assert (newUser.displayName is not None)
        assert (newUser.mailNickname is not None)
        assert (newUser.userPrincipalName is not None)
        assert (newUser.passwordProfile is not None)

        json = newUser.json
        response = self.__postAPI__(edgeEnd="", json=json)
        if response.ok:
            respJson = response.json()
            user = data.User()
            user.fromResponse(data=respJson)
            return user
        else:
            print(f'Request Error{response.text}')
            return None

    def listUsers(self) -> [data.User]:
        response = self.__getAPI__()
        if response.ok:
            respData = response.json()
            usersData = respData.get("value")
            users = []
            for userData in usersData:
                user = data.User()
                user.fromResponse(data=userData)
                users.append(user)
            return users
        else:
            print(f'Request Error{response.text}')
            return None
