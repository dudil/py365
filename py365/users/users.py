import datetime
import random
import string
import uuid
from dataclasses import dataclass
from enum import Enum

from .. import AppConnection
from .. import utils


class AgeGroup(Enum):
    null: "null"
    minor: "minor"
    notAdult: "notAdult"
    adult: "adult"


class ConsentProvidedForMinor(Enum):
    null: "null"
    granted: "granted"
    denied: "denied"
    notRequired: "notRequired"


class LegalAgeGroupClassification(Enum):
    null: "null"
    minorWithOutParentalConsent: "minorWithOutParentalConsent"
    minorWithParentalConsent: "minorWithParentalConsent"
    minorNoParentalConsentRequired: "minorNoParentalConsentRequired"
    notAdult: "notAdult"
    adult: "adult"


# https://docs.microsoft.com/en-us/graph/api/resources/assignedlicense
@dataclass
class AssignedLicense:
    disabledPlans: [uuid.UUID]
    skuId: uuid.UUID

    def payload(self):
        payload = {
            "disabledPlans": self.disabledPlans,
            "skuId": self.skuId
        }
        return payload


# https://docs.microsoft.com/en-us/graph/api/resources/assignedplan
@dataclass
class AssignedPlan:
    assignedDateTime: datetime
    capabilityStatus: str
    service: str
    servicePlanId: uuid.UUID

    def payload(self):
        payload = {
            "assignedDateTime": self.assignedDateTime,
            "capabilityStatus": self.capabilityStatus,
            "service": self.service,
            "servicePlanId": self.servicePlanId
        }
        return payload


# https://docs.microsoft.com/en-us/graph/api/resources/licenseassignmentstate
@dataclass
class LicenseAssignmentState:
    assignedByGroup: str
    disablePlans: [str]
    error: str
    skuId: str
    state: str

    def payload(self):
        payload = {
            "assignedByGroup": self.assignedByGroup,
            "disablePlans": self.disablePlans,
            "error": self.error,
            "skuId": self.skuId,
            "state": self.state
        }
        return payload


# https://docs.microsoft.com/en-us/graph/api/resources/mailboxsettings
# TODO: set properties to correct objects
@dataclass
class MailboxSettings:
    archiveFolder: str
    automaticRepliesSetting: any
    language: any
    timeZone: str
    workingHours: any

    def payload(self):
        payload = {
            "archiveFolder": self.archiveFolder,
            "automaticRepliesSetting": self.automaticRepliesSetting,
            "language": self.language,
            "timeZone": self.timeZone,
            "workingHours": self.workingHours
        }
        return payload


# https://docs.microsoft.com/en-us/graph/api/resources/passwordprofile?view=graph-rest-1.0
@dataclass
class PasswordProfile:
    forceChangePasswordNextSignIn: bool
    password: str = None
    forceChangePasswordNextSignInWithMfa: bool = None

    def payload(self):
        payload: dict = {}
        payload = utils.addPayloadParam(
            payload, "forceChangePasswordNextSignIn", self.forceChangePasswordNextSignIn)
        payload = utils.addPayloadParam(
            payload, "forceChangePasswordNextSignInWithMfa", self.forceChangePasswordNextSignInWithMfa)
        payload = utils.addPayloadParam(
            payload, "password", self.password)
        return payload

    def generateFirstPassword(self, pwLen: int = 10):
        """Generate a random password """
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


# https://docs.microsoft.com/en-us/graph/api/resources/user
@dataclass
class User:
    aboutMe: str = None
    accountEnabled: bool = None
    ageGroup: AgeGroup = None
    assignedLicenses: [AssignedLicense] = None
    assignedPlans: [AssignedPlan] = None
    birthday: datetime = None
    businessPhones: [str] = None
    city: str = None
    companyName: str = None
    consentProvidedForMinor: ConsentProvidedForMinor = None
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
    isResourceAccount: bool = None
    otherMails: [str] = None
    jobTitle: str = None
    legalAgeGroupClassification: LegalAgeGroupClassification = None
    licenseAssignmentStates: [LicenseAssignmentState] = None
    mail: str = None
    mailboxSettings: MailboxSettings = None
    mailNickname: str = None
    mobilePhone: str = None
    mySite: str = None
    passwordProfile: PasswordProfile = None
    onPremisesImmutableId: str = None
    usageLocation: str = None
    officeLocation: str = None
    preferredLanguage: str = None
    surname: str = None
    userPrincipalName: str = None
    id: str = None

    def payload(self) -> dict:
        payload: dict = {}
        payload = utils.addPayloadParam(
            payload, "accountEnabled", self.accountEnabled)
        payload = utils.addPayloadParam(
            payload, "mailNickname", self.mailNickname)
        payload = utils.addPayloadParam(
            payload, "userPrincipalName", self.userPrincipalName)
        payload = utils.addPayloadParam(
            payload, "businessPhones", self.businessPhones)
        payload = utils.addPayloadParam(
            payload, "city", self.city)
        payload = utils.addPayloadParam(
            payload, "companyName", self.companyName)
        payload = utils.addPayloadParam(
            payload, "country", self.country)
        payload = utils.addPayloadParam(
            payload, "department", self.department)
        payload = utils.addPayloadParam(
            payload, "displayName", self.displayName)
        payload = utils.addPayloadParam(
            payload, "givenName", self.givenName)
        payload = utils.addPayloadParam(
            payload, "otherMails", self.otherMails)
        payload = utils.addPayloadParam(
            payload, "jobTitle", self.jobTitle)
        payload = utils.addPayloadParam(
            payload, "usageLocation", self.usageLocation)
        payload = utils.addPayloadParam(
            payload, "officeLocation", self.officeLocation)
        payload = utils.addPayloadParam(
            payload, "surname", self.surname)
        payload = utils.addPayloadParam(
            payload, "passwordProfile", self.passwordProfile.payload())
        payload = utils.addPayloadParam(
            payload, "onPremisesImmutableId", self.onPremisesImmutableId)
        return payload

    @classmethod
    def userFromResponse(cls, userData: dict):
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
        user.id = userData.get("id")

        return user


class Users:
    def __init__(self, connection: AppConnection):
        self.__USERS_ENDPOINT = '/users/'
        self.connection = connection

    '''
    lookupby is either user AAD id or user Priniciapl Name (login username)
    '''

    def getUser(self, lookupby: str):
        lookupEndpoint = self.__USERS_ENDPOINT + lookupby
        response = self.connection.get(lookupEndpoint)
        # TODO check for valid response
        if response.ok:
            print(f'User Name is: {response.json().get("displayName", "ERROR")}')
        else:
            print(f'Request Error{response.text}')

        # initialise 
        respJson = response.json()
        user = User.userFromResponse(respJson)

        return user

    '''
    lookupby is either user AAD id or user Principal Name (login username)
    '''

    def updateUser(self, lookupby: str, userData: User):
        lookupEndpoint = self.__USERS_ENDPOINT + lookupby
        response = self.connection.patch(lookupEndpoint, userData.payload())

        return response

    def createUser(self, newUser: User):
        endpoint = self.__USERS_ENDPOINT

        assert (newUser.accountEnabled is not None)
        assert (newUser.displayName is not None)
        assert (newUser.mailNickname is not None)
        assert (newUser.userPrincipalName is not None)
        assert (newUser.passwordProfile is not None)

        response = self.connection.post(endpoint=endpoint, json=newUser.payload())

        return response
