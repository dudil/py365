"""Enums use by the users edge"""

# TODO: Move to the resource folder
'''
# https://docs.microsoft.com/en-us/graph/api/resources/assignedplan
class AssignedPlan:
    assignedDateTime: datetime
    capabilityStatus: str
    service: str
    servicePlanId: uuid.UUID

    def payload( self ):
        payload = {
            "assignedDateTime": self.assignedDateTime,
            "capabilityStatus": self.capabilityStatus,
            "service": self.service,
            "servicePlanId": self.servicePlanId
        }
        return payload


# https://docs.microsoft.com/en-us/graph/api/resources/licenseassignmentstate
class LicenseAssignmentState:
    assignedByGroup: str
    disablePlans: [str]
    error: str
    skuId: str
    state: str

    def payload( self ):
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
class MailboxSettings:
    archiveFolder: str
    automaticRepliesSetting: any
    language: any
    timeZone: str
    workingHours: any
'''
