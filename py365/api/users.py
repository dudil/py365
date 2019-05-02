"""
https://docs.microsoft.com/en-us/graph/api/resources/users
"""
from py365 import auth, rsc


class Users(object):
    """
    You can use Microsoft Graph365 to build compelling app experiences based on users,
    their relationships with other users and groups, and their mail, calendar, and files.

    You can access users through Microsoft Graph365 in two ways:

    * By their ID, /users/{id | userPrincipalName}
    * By using the /me alias for the signed-in user, which is the same as /users/{signed-in user's id}
    """

    class User(object):
        """
        Class User is the user edge related to user operations
        """

        # user key can be either id or login mail
        def __init__(self, connection: auth.AppConnection, userKey: str):
            self.connection = connection
            self.userKey = userKey
            self.__USER_ENDPOINT = f'/users/{userKey}'

        def getUser(self) -> rsc.User:
            """
            https://docs.microsoft.com/en-us/graph/api/user-get
            Retrieve the properties and relationships of user object.

            :return: the found user object
            :rtype: User
            """
            lookupEndpoint = self.__USER_ENDPOINT
            response = self.connection.get(lookupEndpoint)
            if response.ok:
                respJson = response.json()
                user = rsc.User.userFromResponse(respJson)
                return user
            else:
                print(f'Request Error{response.text}')
                return None

        def updateUser(self, userData: rsc.User) -> rsc.User:
            """
            https://docs.microsoft.com/en-us/graph/api/user-update
            Update the properties of a user object.

            :param userData:
            :type userData:
            :return:
            :rtype:
            """
            endpoint = self.__USER_ENDPOINT
            response = self.connection.patch(endpoint, userData.payload)

            if response.ok:
                respJson = response.json()
                user = rsc.User.userFromResponse(respJson)
                return user
            else:
                print(f'Request Error{response.text}')
                return None

        def sendMail(self, message: rsc.BaseMessage, saveToSentItems: bool = True):
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
            endpoint = self.__USER_ENDPOINT + '/sendMail'
            payload = {
                "message": message.payload,
                "saveToSentItems": saveToSentItems
            }
            response = self.connection.post(endpoint=endpoint, json=payload)

            return response

    def __init__(self, connection: auth.AppConnection):
        """
        Initialisation method for the *Users* class
        :param connection: graph connection
        :type connection: AppConnection
        """
        self.__USERS_ENDPOINT = '/users/'
        self.connection = connection

    def user(self, userKey: str) -> User:
        """
        This method represent a user API edge following the Users edge
        NB! Not to confuse with the rsc.User class which is critical to the graph operation.
        Why MS decided on that (kind of strange) flow, is not very clear to me.
        A better design would be probably to make the User API as major instead of Users/UserID
        Users, would match better a group of users where the default group is all.
        This would make it more meaningful and simple... Anyway....
        :param userKey: The user identification key; could be the user object tenant id or the principal name (login id)
        :type userKey: str
        :return: a User API object that will handle a specific user API operations
        :rtype: Users -> User subclass
        """
        userAPI = self.User(connection=self.connection, userKey=userKey)
        return userAPI

    def createUser(self, newUser: rsc.User) -> rsc.User:
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
        endpoint = self.__USERS_ENDPOINT

        assert (newUser.accountEnabled is not None)
        assert (newUser.displayName is not None)
        assert (newUser.mailNickname is not None)
        assert (newUser.userPrincipalName is not None)
        assert (newUser.passwordProfile is not None)

        json = newUser.payload
        response = self.connection.post(endpoint=endpoint, json=json)

        if response.ok:
            respJson = response.json()
            user = rsc.User.userFromResponse(respJson)
            return user
        else:
            print(f'Request Error{response.text}')
            return None
