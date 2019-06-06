""" https://docs.microsoft.com/en-us/graph/api/resources/passwordprofile?view=graph-rest-1.0 """
import random
import string
import attr

from ._base_data import BaseData


@attr.s(auto_attribs=True)
class PasswordProfile(BaseData):
    forceChangePasswordNextSignIn: bool = None
    password: str = None
    forceChangePasswordNextSignInWithMfa: bool = None

    def generateRandomPassword(self, pwLen: int = 10):
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
