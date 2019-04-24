"""
https://docs.microsoft.com/en-us/graph/api/resources/users
"""
from core.app_connection import AppConnection
from users.user import User


class Users(object):
    """
    You can use Microsoft Graph to build compelling app experiences based on users,
    their relationships with other users and groups, and their mail, calendar, and files.

    You can access users through Microsoft Graph in two ways:

    * By their ID, /users/{id | userPrincipalName}
    * By using the /me alias for the signed-in user, which is the same as /users/{signed-in user's id}
    """
    def __init__(self, connection: AppConnection):
        self.__USERS_ENDPOINT = '/users/'
        self.connection = connection

    '''
    lookUpBy is either user AAD id or user Principal Name (login username)
    '''

    def getUser( self, lookUpBy: str ) -> User:
        """
        https://docs.microsoft.com/en-us/graph/api/user-get
        Retrieve the properties and relationships of user object.

        :param lookUpBy: the uid or principal name of the user to look for
        :type lookUpBy: str
        :return: the found user object
        :rtype: User
        """
        lookupEndpoint = self.__USERS_ENDPOINT + lookUpBy
        response = self.connection.get(lookupEndpoint)
        if response.ok:
            respJson = response.json()
            user = User.userFromResponse(respJson)
            return user
        else:
            print(f'Request Error{response.text}')
            return None

    '''
    lookUpBy is either user AAD id or user Principal Name (login username)
    '''

    def updateUser( self, lookUpBy: str, userData: User ) -> User:
        """
        https://docs.microsoft.com/en-us/graph/api/user-update
        Update the properties of a user object.
        :param lookUpBy:
        :type lookUpBy:
        :param userData:
        :type userData:
        :return:
        :rtype:
        """
        lookupEndpoint = self.__USERS_ENDPOINT + lookUpBy
        response = self.connection.patch(lookupEndpoint, userData.payload())

        if response.ok:
            respJson = response.json()
            user = User.userFromResponse(respJson)
            return user
        else:
            print(f'Request Error{response.text}')
            return None

    def createUser( self, newUser: User ) -> User:
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

        json = newUser.payload()
        response = self.connection.post(endpoint=endpoint, json=json)

        if response.ok:
            respJson = response.json()
            user = User.userFromResponse(respJson)
            return user
        else:
            print(f'Request Error{response.text}')
            return None
