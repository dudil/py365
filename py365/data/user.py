"""
https://docs.microsoft.com/en-us/graph/api/resources/user
"""
import attr
import datetime
from .directory_object import DirectoryObject
from .password_profile import PasswordProfile


@attr.s(auto_attribs=True)
class User(DirectoryObject):
    """
    # user resource type

    Represents an Azure AD user account. Inherits from directoryObject.

    This resource supports:

    * Adding your own data to custom properties as extensions.
    * Subscribing to change notifications.
    * Using delta query to track incremental additions, deletions, and updates, by providing a delta function.
    """

    aboutMe: str = None
    accountEnabled: bool = None
    birthday: datetime = None
    businessPhones: [str] = None
    city: str = None
    companyName: str = None
    country: str = None
    createdDateTime: datetime = None
    department: str = None
    displayName: str = None
    employeeId: str = None
    faxNumber: str = None
    givenName: str = None
    hireDate: datetime = None
    imAddresses: [str] = None
    interests: [str] = None
    otherMails: [str] = None
    jobTitle: str = None
    mail: str = None
    mailNickname: str = None
    mobilePhone: str = None
    passwordProfile: PasswordProfile = None
    usageLocation: str = None
    officeLocation: str = None
    surname: str = None
    userPrincipalName: str = None
