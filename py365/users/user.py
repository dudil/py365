from dataclasses import dataclass
from enum import Enum
import uuid
import datetime
from .. import AppConnection

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
class UserData:
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
    id: str = None
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

    

class User:
    # Class Private Consts
    __USERS_ENDPOINT = '/users/'

    def __init__(self, lookup: str, connection: AppConnection):
        self.lookup = lookup
        self.connection = connection


    @classmethod
    def byId(cls, id: str, connection: AppConnection):
        return cls(lookup=id, connection=connection)


    @classmethod
    def byUserPrincipalName(cls, userPrincipalName: str, connection: AppConnection):
        return cls(lookup=userPrincipalName, connection=connection)

    def getUser(self):
        lookupEndpoint = self.__USERS_ENDPOINT + self.lookup
        response = self.connection.get(lookupEndpoint)
        #TODO check for valid reponse
        if response.ok:
            print(f'User Name is: {response.json().get("displayName", "ERROR")}')
        else:
            print(f'Request Error{response.text}')

        # initialise UserData
        userData = UserData()
        respJson = response.json()
        userData.businessPhones = respJson.get("businessPhones")
        userData.displayName = respJson.get("displayName")
        userData.givenName = respJson.get("givenName")
        userData.jobTitle = respJson.get("jobTitle")
        userData.mail = respJson.get("mail")
        userData.mobilePhone = respJson.get("mobilePhone")
        userData.officeLocation = respJson.get("officeLocation")
        userData.preferredLanguage = respJson.get("preferredLanguage")
        userData.surname = respJson.get("surname")
        userData.userPrincipalName = respJson.get("userPrincipalName")
        userData.id = respJson.get("id")

        return userData








