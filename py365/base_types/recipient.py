from dataclasses import dataclass
from . import EmailAddress

# https://docs.microsoft.com/en-us/graph/api/resources/recipient
@dataclass
class Recipient:
    emailAddress: EmailAddress

    def __repr__(self):
        repr = {
            "emailAddress": emailAddress
        }
        return repr
