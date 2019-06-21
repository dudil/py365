"""
https://docs.microsoft.com/en-us/graph/api/resources/group?view=graph-rest-1.0
"""
import attr
import datetime
from .assigned_license import AssignedLicense
from .user import User
from .directory_object import DirectoryObject
from .on_premises_provisioning_error import OnPremisesProvisioningError
from py365.enums import GroupType, GroupCategory, GroupVisibility


@attr.s(auto_attribs=True)
class Group(DirectoryObject):
    """
    # group resource type

    TODO: add more information
    """

    # Group Properties
    allowExternalSenders: bool = None
    assignedLicenses: [AssignedLicense] = None
    autoSubscribeNewMembers: bool = None
    classification: str = None  # TODO: Check if enum
    createdDateTime: datetime = None
    description: str = None
    displayName: str = None
    groupTypes: [GroupType] = None
    hasMembersWithLicenseErrors: bool = None
    isSubscribedByMail: bool = None
    licenseProcessingState: str = None
    mail: str = None
    mailEnabled: bool = None
    mailNickname: str = None
    onPremisesLastSyncDateTime: datetime = None
    onPremisesProvisioningErrors: [OnPremisesProvisioningError] = None
    onPremisesSecurityIdentifier: str = None
    onPremisesSyncEnabled: bool = None
    preferredDataLocation: str = None
    proxyAddresses: [str] = None
    renewedDateTime: datetime = None
    securityEnabled: bool = None
    unseenCount: int = None
    visibility: GroupVisibility = None

    # Group Relationships
    acceptedSenders: [DirectoryObject] = None
    # calendar: Calendar = None
    # calendarView: [Event] = None
    # conversations: [Conversation] = None
    createdOnBehalfOf: DirectoryObject = None
    # drive: Drive = None
    # drives: [Drive] = None
    # events: [Event] = None
    # extensions: [Extension] = None
    # groupLifecyclePolicies: [GroupLifecyclePolicy] = None
    memberOf: [DirectoryObject] = None
    members: [DirectoryObject] = None
    membersWithLicenseErrors: [User] = None
    # onenote: Onenote = None
    owners: [DirectoryObject] = None
    # photo: ProfilePhoto = None
    # photos: [ProfilePhoto] = None
    # planner: PlannerGroup = None
    rejectedSenders: [DirectoryObject] = None

    # settings: [GroupSetting] = None
    # sites: [Site] = None
    # threads: [ConversationThread] = None

    @property
    def category(self) -> GroupCategory:
        """
        Logic is per the following URL
        https://docs.microsoft.com/en-us/graph/api/resources/groups-overview
        :return: The Group Category
        :rtype: GroupCategory
        """
        if GroupType.UNIFIED.value in self.groupTypes:
            return GroupCategory.OFFICE_365
        elif self.mailEnabled is False:
            return GroupCategory.SECURITY
        elif self.securityEnabled is True:
            return GroupCategory.MAIL_ENABLED_SECURITY
        else:
            return GroupCategory.DISTRIBUTION

    @category.setter
    def category(self, groupCategory: GroupCategory):
        self.groupTypes = []
        if groupCategory is GroupCategory.OFFICE_365:
            self.groupTypes.append(GroupType.UNIFIED.value)
            self.mailEnabled = True
            self.securityEnabled = False
        elif groupCategory is GroupCategory.SECURITY:
            self.mailEnabled = False
            self.securityEnabled = True
        elif groupCategory is GroupCategory.MAIL_ENABLED_SECURITY:
            self.mailEnabled = True
            self.securityEnabled = True
        else:  # GroupCategory.DISTRIBUTION
            self.mailEnabled = True
            self.securityEnabled = False
