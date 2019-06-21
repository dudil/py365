"""
https://docs.microsoft.com/en-us/graph/api/resources/group
"""
from py365 import auth, data, enums
from ._base_resource import BaseResource


class Groups(BaseResource):
    """
    Represents an Azure Active Directory (Azure AD) group, which can be an Office 365 group, or a security group.

    This resource supports:
    * Adding your own data to custom properties as extensions.
    * Subscribing to change notifications.
    * Using delta query to track incremental additions, deletions, and updates, by providing a delta function.
    """

    class Group(BaseResource):

        def __init__(self, connection: auth.AppConnection, groupId: str):
            self.groupId = groupId
            BaseResource.__init__(self, connection=connection, endpoint=f'/groups/{groupId}')

        def listPlans(self) -> [data.PlannerPlan]:
            endpoint = self.ENDPOINT + '/planner/plans'
            response = self.connection.get(endpoint=endpoint)
            if response.ok:
                respData = response.json()
                plansData = respData.get("value")
                plans = []
                for planData in plansData:
                    plan = data.PlannerPlan()
                    plan.fromResponse(data=planData)
                    plans.append(plan)
                return plans
            else:
                print(f'Request Error{response.text}')
                return None

    def __init__(self, connection: auth.AppConnection):
        BaseResource.__init__(self, connection, '/groups')

    def group(self, groupId) -> Group:
        groupAPI = Groups.Group(connection=self.connection, groupId=groupId)
        return groupAPI

    def createGroup(self, newGroup: data.Group) -> data.Group:
        assert (newGroup.displayName is not None)  # The name to display in the address book for the group. Required.
        assert (newGroup.mailEnabled is not None)  # Set to true for mail-enabled groups. Required.
        assert (newGroup.mailNickname is not None)  # The mail alias for the group. Required.
        assert (newGroup.securityEnabled is not None)  # Set to true for security-enabled groups. Required.
        #  assert(newGroup.owners is not None)  # The owners for the group at creation time. Optional.
        #  assert(newGroup.members is not None)  # The members for the group at creation time. Optional.
        assert (newGroup.groupTypes is not None)  # Control the type of group and its membership

        json = newGroup.json
        response = self.connection.post(endpoint=self.ENDPOINT, json=json)

        group: data.Group = data.Group()
        if response.ok:
            respJson = response.json()
            group.fromResponse(data=respJson)
        else:
            print(f'Request Error{response.text}')

        return group

    def createGroupByCategory(self, groupCategory: enums.GroupCategory, displayName: str, mailNickname: str
                              , visibility: enums.GroupVisibility, owners: [data.DirectoryObject]
                              , members: [data.DirectoryObject] = None, description: str = None
                              , allowExternalSenders: bool = False, isSubscribedByMail: bool = True) -> data.Group:
        newGroup = data.Group()
        newGroup.category = groupCategory
        newGroup.displayName = displayName
        newGroup.mailNickname = mailNickname
        newGroup.owners = owners
        newGroup.members = members
        newGroup.allowExternalSenders = allowExternalSenders
        newGroup.description = description
        newGroup.isSubscribedByMail = isSubscribedByMail
        newGroup.visibility = visibility

        return self.createGroup(newGroup=newGroup)

    def listGroups(self) -> [data.Group]:
        """
        List all the groups available in an organization, including but not limited to Office 365 Groups.

        :return:
        :rtype:
        """
        response = self.connection.get(endpoint=self.ENDPOINT)
        if response.ok:
            respData = response.json()
            groupsData = respData.get("value")
            groups = []
            for groupData in groupsData:
                group = data.Group()
                group.fromResponse(data=groupData)
                groups.append(group)
            return groups
        else:
            print(f'Request Error{response.text}')
            return None
