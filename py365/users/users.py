from dataclasses import dataclass
from enum import Enum
import uuid
import datetime

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

    def __repr__(self):
        repr = {
            "disabledPlans": disabledPlans,
            "skuId": skuId
        }
        return repr


# https://docs.microsoft.com/en-us/graph/api/resources/assignedplan
@dataclass
class AssignedPlan:
    assignedDateTime: datetime
    capabilityStatus: str
    service: str
    servicePlanId: uuid.UUID

    def __repr__(self):
        repr = {
            "assignedDateTime": assignedDateTime,
            "capabilityStatus": capabilityStatus,
            "service": service,
            "servicePlanId": servicePlanId
        }
        return repr

# https://docs.microsoft.com/en-us/graph/api/resources/licenseassignmentstate
@dataclass
class LicenseAssignmentState:
    assignedByGroup: str
    disablePlans: [str]
    error: str
    skuId: str
    state: str


    def __repr__(self):
        repr = {
            "assignedByGroup": assignedByGroup,
            "disablePlans": disablePlans,
            "error": error,
            "skuId": skuId,
            "state": state
        }
        return repr

# https://docs.microsoft.com/en-us/graph/api/resources/mailboxsettings
#TODO: set properties to correct objects
@dataclass
class MailboxSettings:
    archiveFolder: str
    automaticRepliesSetting: any
    language: any
    timeZone: str
    workingHours: any

    def __repr__(self):
        repr = {
            "archiveFolder": archiveFolder,
            "automaticRepliesSetting": automaticRepliesSetting,
            "language": language,
            "timeZone": timeZone,
            "workingHours": workingHours
        }


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
    jobTitle: str = None
    legalAgeGroupClassification: LegalAgeGroupClassification = None
    licenseAssignmentStates: [LicenseAssignmentState] = None
    mail: str = None
    mailboxSettings: MailboxSettings = None
    mailNickname: str = None
    mobilePhone: str = None
    mySite: str = None
    officeLocation: str = None
    preferredLanguage: str = None
    surname: str = None
    userPrincipalName: str = None
    id: str = None

    def toPayload(self):
        payload = {}
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
            payload, "jobTitle", self.jobTitle)
        payload = utils.addPayloadParam(
            payload, "officeLocation", self.officeLocation)
        payload = utils.addPayloadParam(
            payload, "surname", self.surname)
        return payload

    @classmethod
    def userFromResponse(cls, userData:dict):
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
    def getUser(self, lookupby :str):
        lookupEndpoint = self.__USERS_ENDPOINT + lookupby
        response = self.connection.get(lookupEndpoint)
        #TODO check for valid reponse
        if response.ok:
            print(f'User Name is: {response.json().get("displayName", "ERROR")}')
        else:
            print(f'Request Error{response.text}')

        # initialise 
        respJson = response.json()
        user = User.userFromResponse(respJson)

        return user
        
    '''
    lookupby is either user AAD id or user Priniciapl Name (login username)
    '''
    def updateUser(self, lookupby: str, userData: User):
        lookupEndpoint = self.__USERS_ENDPOINT + lookupby
        response = self.connection.patch(lookupEndpoint, userData.toPayload())

        return response
        








