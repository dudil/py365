from dataclasses import dataclass

# https://docs.microsoft.com/en-us/graph/api/resources/emailaddress
@dataclass
class EmailAddress:
    adress: str
    name: str

    def __repr__(self):
        repr = {
            "address": adress, 
            "name": name
            }
        return repr