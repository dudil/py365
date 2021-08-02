""" https://docs.microsoft.com/en-us/graph/api/resources/passwordprofile?view=graph-rest-1.0 """
import random
import string
from pydantic import BaseModel


class PasswordProfile(BaseModel):
    forceChangePasswordNextSignIn: bool = None
    password: str = None
    forceChangePasswordNextSignInWithMfa: bool = None

    def generate_random_password(self, pwLen: int = 10) -> str:
        """
        Generate Random Password to use
        :param pwLen: the password length (optional)
        :type pwLen: int
        """
        random_source = string.ascii_letters + string.digits + string.punctuation
        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
        for i in range(pwLen):
            password += random.choice(random_source)
        password_list = list(password)
        random.SystemRandom().shuffle(password_list)
        password = "".join(password_list)
        self.password = password
        return password
