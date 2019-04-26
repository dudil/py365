"""
https://docs.microsoft.com/en-us/graph/api/resources/user
"""
import datetime

from ._base_resource import BaseResource
from .password_profile import PasswordProfile


# TODO: Move to the resource folder
class User(BaseResource):
    """
    # user resource type

    Represents an Azure AD user account. Inherits from directoryObject.

    This resource supports:

    * Adding your own data to custom properties as extensions.
    * Subscribing to change notifications.
    * Using delta query to track incremental additions, deletions, and updates, by providing a delta function.
    """

    def __init__( self,
                  aboutMe: str = None,
                  accountEnabled: bool = None,
                  birthday: datetime = None,
                  businessPhones: [str] = None,
                  city: str = None,
                  companyName: str = None,
                  country: str = None,
                  createdDateTime: datetime = None,
                  department: str = None,
                  displayName: str = None,
                  employeeId: str = None,
                  faxNumber: str = None,
                  givenName: str = None,
                  hireDate: datetime = None,
                  imAddresses: [str] = None,
                  interests: [str] = None,
                  otherMails: [str] = None,
                  jobTitle: str = None,
                  # licenseAssignmentStates: [\LicenseAssignmentState] = None,
                  # assignedLicenses: [AssignedLicense] = None,
                  # assignedPlans: [AssignedPlan] = None,
                  # mailboxSettings: MailboxSettings = None,
                  mail: str = None,
                  mailNickname: str = None,
                  mobilePhone: str = None,
                  passwordProfile: PasswordProfile = None,
                  usageLocation: str = None,
                  officeLocation: str = None,
                  surname: str = None,
                  userPrincipalName: str = None,
                  uid: str = None ):
        self.aboutMe: str = aboutMe
        self.accountEnabled: bool = accountEnabled
        self.birthday: datetime = birthday
        self.businessPhones: [str] = businessPhones
        self.city: str = city
        self.companyName: str = companyName
        self.country: str = country
        self.createdDateTime: datetime = createdDateTime
        self.department: str = department
        self.displayName: str = displayName
        self.employeeId: str = employeeId
        self.faxNumber: str = faxNumber
        self.givenName: str = givenName
        self.hireDate: datetime = hireDate
        self.imAddresses: [str] = imAddresses
        self.interests: [str] = interests
        self.otherMails: [str] = otherMails
        self.jobTitle: str = jobTitle
        self.mail: str = mail
        self.mailNickname: str = mailNickname
        self.mobilePhone: str = mobilePhone
        self.passwordProfile: PasswordProfile = passwordProfile
        self.usageLocation: str = usageLocation
        self.officeLocation: str = officeLocation
        self.surname: str = surname
        self.userPrincipalName: str = userPrincipalName
        self.uid: str = uid
        BaseResource.__init__(self)

    @classmethod
    def userFromResponse( cls, userData: dict ):
        """
        create a user object from an OG operation response
        :param userData: the user data received from the OG operation
        :type userData: dict
        :return: The created user object
        :rtype: User
        """
        user = cls()
        user.businessPhones = userData.get("businessPhones")
        user.displayName = userData.get("displayName")
        user.givenName = userData.get("givenName")
        user.jobTitle = userData.get("jobTitle")
        user.mail = userData.get("mail")
        user.mobilePhone = userData.get("mobilePhone")
        user.officeLocation = userData.get("officeLocation")
        user.preferredLanguage = userData.get("preferredLanguage")
        user.surname = userData.get("surname")
        user.userPrincipalName = userData.get("userPrincipalName")
        user.uid = userData.get("id")

        return user
