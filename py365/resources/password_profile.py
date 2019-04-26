""" https://docs.microsoft.com/en-us/graph/api/resources/passwordprofile?view=graph-rest-1.0 """
import random
import string

from ._base_resource import BaseResource


class PasswordProfile(BaseResource):
    """
    Password profile OG resource - use to set a password and password behaviour for users
    :param forceChangePasswordNextSignIn: should the user change the password upon first login
    :param password: the user password
    :param forceChangePasswordNextSignInWithMfa: should the next sign will be with MFA
    """

    def __init__( self, forceChangePasswordNextSignIn: bool = None, password: str = None
                  , forceChangePasswordNextSignInWithMfa: bool = None ):
        self.forceChangePasswordNextSignIn: bool = forceChangePasswordNextSignIn
        self.password: str = password
        self.forceChangePasswordNextSignInWithMfa: bool = forceChangePasswordNextSignInWithMfa
        BaseResource.__init__(self)

    def generateFirstPassword( self, pwLen: int = 10 ):
        """
        Generate Random Password to use
        :param pwLen: the password length (optional)
        :type pwLen: int
        """
        randomSource = string.ascii_letters + string.digits + string.punctuation
        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
        for i in range(pwLen):
            password += random.choice(randomSource)
        passwordList = list(password)
        random.SystemRandom().shuffle(passwordList)
        password = ''.join(passwordList)
        self.password = password
