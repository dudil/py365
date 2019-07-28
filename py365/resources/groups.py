"""
https://docs.microsoft.com/en-us/graph/api/resources/group
"""
from py365 import auth, data, enums
from ._base_resource import BaseResource
from ._child_resource import ChildResource


class Groups(BaseResource):
    """
    Represents an Azure Active Directory (Azure AD) group, which can be an Office 365 group, or a security group.

    This resource supports:
    * Adding your own data to custom properties as extensions.
    * Subscribing to change notifications.
    * Using delta query to track incremental additions, deletions, and updates, by providing a delta function.
    """

    class Group(ChildResource):

        def __init__(self, groupsAPI: BaseResource, groupId: str):
            self.groupId = groupId
            super().__init__(baseAPI=groupsAPI, edgeMid=f'/{groupId}')

        def listPlans(self) -> [data.PlannerPlan]:
            edgeEnd = '/planner/plans'
            response = self.__getAPI__(edgeEnd=edgeEnd)
            plans = []
            if response.ok:
                respData = response.json()
                plansData = respData.get("value")
                for planData in plansData:
                    plan = data.PlannerPlan()
                    plan.fromResponse(data=planData)
                    plans.append(plan)
            else:
                print(f'Request Error {response.text}')
            return plans

        def updateGroup(self, updateData: data.Group) -> bool:
            json = updateData.json
            response = self.__patchAPI__(json=json)
            if response.ok:
                retCode = True
            else:
                print(f'Request Error {response.text}')
                retCode = False
            return retCode

        def _listUsers(self, userType: enums.GroupUserTypes) -> [data.DirectoryObject]:
            if userType is enums.GroupUserTypes.MEMBER:
                edgeEnd = '/members'
            elif userType is enums.GroupUserTypes.OWNER:
                edgeEnd = '/owners'
            else:
                raise Exception(f"Not supported user type: {type}")

            response = self.__getAPI__(edgeEnd=edgeEnd)
            users: [data.DirectoryObject] = []
            if response.ok:
                dirObjects = response.json().get("value")
                for dirObject in dirObjects:
                    user = data.DirectoryObject()
                    user.fromResponse(data=dirObject)
                    users.append(user)
            else:
                print(f'Request Error {response.text}')
            return users

        def listMembers(self) -> [data.DirectoryObject]:
            """
            https://docs.microsoft.com/en-us/graph/api/group-list-members
            :return:
            :rtype:
            """
            return self._listUsers(enums.GroupUserTypes.MEMBER)

        def listOwners(self) -> [data.DirectoryObject]:
            """
            https://docs.microsoft.com/en-us/graph/api/group-list-owners
            :return:
            :rtype:
            """
            return self._listUsers(enums.GroupUserTypes.Owner)

        def _addUser(self, userType: enums.GroupUserTypes, user: data.DirectoryObject):
            if userType is enums.GroupUserTypes.MEMBER:
                edgeEnd = '/members/$ref'
            elif userType is enums.GroupUserTypes.OWNER:
                edgeEnd = '/owners/$ref'
            else:
                raise Exception(f"Not supported user type: {type}")

            json = {"@odata.id": user.odata_id}
            response = self.__postAPI__(edgeEnd=edgeEnd, json=json)
            if response.ok:
                pass
            else:
                print(f'Request Error {response.text}')

        def addMember(self, member: data.DirectoryObject):
            """
            https://docs.microsoft.com/en-us/graph/api/group-post-members
            :param member:
            :type member:
            :return:
            :rtype:
            """
            self._addUser(enums.GroupUserTypes.MEMBER, member)

        def addOwner(self, owner: data.DirectoryObject):
            """
            https://docs.microsoft.com/en-us/graph/api/group-post-owners
            :param owner:
            :type owner:
            :return:
            :rtype:
            """
            self._addUser(enums.GroupUserTypes.OWNER, owner)

    def __init__(self, connection: auth.AppConnection):
        super().__init__(connection, '/groups')

    def group(self, groupId) -> Group:
        groupAPI = Groups.Group(groupsAPI=self, groupId=groupId)
        return groupAPI

    def createGroup(self, newGroup: data.Group) -> data.Group:
        assert (newGroup.displayName is not None)  # The name to display in the address book for the group. Required.
        assert (newGroup.mailEnabled is not None)  # Set to true for mail-enabled groups. Required.
        assert (newGroup.mailNickname is not None)  # The mail alias for the group. Required.
        assert (newGroup.securityEnabled is not None)  # Set to true for security-enabled groups. Required.
        #  assert(newGroup.owners is not None)  # The owners for the group at creation time. Optional.
        #  assert(newGroup.members is not None)  # The members for the group at creation time. Optional.
        assert (newGroup.groupTypes is not None)  # Control the type of group and its membership

        members = newGroup.members
        membersDataList = [m.odata_id for m in members]
        owners = newGroup.owners
        ownersDataList = [o.odata_id for o in owners]
        newGroup.members = None
        newGroup.owners = None
        json = newGroup.json

        json.update({"owners@odata.bind": ownersDataList, "members@odata.bind": membersDataList})
        response = self.__postAPI__(json=json)
        if response.ok:
            respJson = response.json()
            newGroup.fromResponse(data=respJson)
        else:
            print(f'Request Error {response.text}')

        return newGroup

    def createGroupByCategory(self, groupCategory: enums.GroupCategory, displayName: str, mailNickname: str
                              , visibility: enums.GroupVisibility, owners: [data.DirectoryObject]
                              , members: [data.DirectoryObject] = None, description: str = None) -> data.Group:
        newGroup = data.Group()
        newGroup.category = groupCategory
        newGroup.displayName = displayName
        newGroup.mailNickname = mailNickname
        newGroup.owners = owners
        newGroup.members = members
        newGroup.description = description
        newGroup.visibility = visibility

        return self.createGroup(newGroup=newGroup)

    def listGroups(self) -> [data.Group]:
        """
        List all the groups available in an organization, including but not limited to Office 365 Groups.

        :return:
        :rtype:
        """
        response = self.__getAPI__()
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
            print(f'Request Error {response.text}')
            return None
