"""
https://docs.microsoft.com/en-us/graph/api/resources/group
"""
from typing import List

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
        def __init__(self, groups_api: BaseResource, group_id: str):
            self.groupId = group_id
            super().__init__(base_api=groups_api, edge_mid=f"/{group_id}")

        def list_plans(self) -> List[data.PlannerPlan]:
            edge_end = "/planner/plans"
            response = self.__get_api__(edge_end=edge_end)
            plans = []
            if response.ok:
                resp_data = response.json()
                plans_data = resp_data.get("value")
                for plan_data in plans_data:
                    plan = data.PlannerPlan.parse_raw(plan_data)
                    plans.append(plan)
            else:
                print(f"Request Error {response.text}")
            return plans

        def update_group(self, update_data: data.Group) -> bool:
            response = self.__patch_api__(data=update_data.dict())
            if response.ok:
                ret_code = True
            else:
                print(f"Request Error {response.text}")
                ret_code = False
            return ret_code

        def _list_users(
            self, user_type: enums.GroupUserTypes
        ) -> [data.DirectoryObject]:
            if user_type is enums.GroupUserTypes.MEMBER:
                edge_end = "/members"
            elif user_type is enums.GroupUserTypes.OWNER:
                edge_end = "/owners"
            else:
                raise Exception(f"Not supported user type: {type}")

            response = self.__get_api__(edge_end=edge_end)
            users: [data.DirectoryObject] = []
            if response.ok:
                dir_objects = response.json().get("value")
                for dir_object in dir_objects:
                    user = data.DirectoryObject.parse_raw(dir_object)
                    users.append(user)
            else:
                print(f"Request Error {response.text}")
            return users

        def list_members(self) -> [data.DirectoryObject]:
            """
            https://docs.microsoft.com/en-us/graph/api/group-list-members
            :return:
            :rtype:
            """
            return self._list_users(enums.GroupUserTypes.MEMBER)

        def list_owners(self) -> [data.DirectoryObject]:
            """
            https://docs.microsoft.com/en-us/graph/api/group-list-owners
            :return:
            :rtype:
            """
            return self._list_users(enums.GroupUserTypes.Owner)

        def _add_user(
            self, user_type: enums.GroupUserTypes, user: data.DirectoryObject
        ):
            if user_type is enums.GroupUserTypes.MEMBER:
                edge_end = "/members/$ref"
            elif user_type is enums.GroupUserTypes.OWNER:
                edge_end = "/owners/$ref"
            else:
                raise Exception(f"Not supported user type: {type}")

            json = {"@odata.id": user.odata_id}
            response = self.__post_api__(edge_end=edge_end, data=json)
            if response.ok:
                pass
            else:
                print(f"Request Error {response.text}")

        def add_member(self, member: data.DirectoryObject):
            """
            https://docs.microsoft.com/en-us/graph/api/group-post-members
            :param member:
            :type member:
            :return:
            :rtype:
            """
            self._add_user(enums.GroupUserTypes.MEMBER, member)

        def add_owner(self, owner: data.DirectoryObject):
            """
            https://docs.microsoft.com/en-us/graph/api/group-post-owners
            :param owner:
            :type owner:
            :return:
            :rtype:
            """
            self._add_user(enums.GroupUserTypes.OWNER, owner)

    def __init__(self, connection: auth.AppConnection):
        super().__init__(connection, "/groups")

    def group(self, group_id) -> Group:
        group_api = Groups.Group(groups_api=self, group_id=group_id)
        return group_api

    def create_group(self, new_group: data.Group) -> data.Group:
        assert (
            new_group.displayName is not None
        )  # The name to display in the address book for the group. Required.
        assert (
            new_group.mailEnabled is not None
        )  # Set to true for mail-enabled groups. Required.
        assert (
            new_group.mailNickname is not None
        )  # The mail alias for the group. Required.
        assert (
            new_group.securityEnabled is not None
        )  # Set to true for security-enabled groups. Required.
        #  assert(new_group.owners is not None)  # The owners for the group at creation time. Optional.
        #  assert(new_group.members is not None)  # The members for the group at creation time. Optional.
        assert (
            new_group.groupTypes is not None
        )  # Control the type of group and its membership

        members = new_group.members
        members_data_list = [m.odata_id for m in members]
        owners = new_group.owners
        owners_data_list = [o.odata_id for o in owners]
        new_group.members = None
        new_group.owners = None
        json = new_group.json

        json.update(
            {
                "owners@odata.bind": owners_data_list,
                "members@odata.bind": members_data_list,
            }
        )
        response = self.__post_api__(data=json)
        if response.ok:
            resp_json = response.json()
            new_group.fromResponse(data=resp_json)
        else:
            print(f"Request Error {response.text}")

        return new_group

    def create_group_by_category(
        self,
        group_category: enums.GroupCategory,
        display_name: str,
        mail_nickname: str,
        visibility: enums.GroupVisibility,
        owners: [data.DirectoryObject],
        members: [data.DirectoryObject] = None,
        description: str = None,
    ) -> data.Group:
        new_group = data.Group()
        new_group.category = group_category
        new_group.displayName = display_name
        new_group.mailNickname = mail_nickname
        new_group.owners = owners
        new_group.members = members
        new_group.description = description
        new_group.visibility = visibility

        return self.create_group(new_group=new_group)

    def list_groups(self) -> [data.Group]:
        """
        List all the groups available in an organization, including but not limited to Office 365 Groups.

        :return:
        :rtype:
        """
        response = self.__get_api__()
        if response.ok:
            resp_data = response.json()
            groups_data = resp_data.get("value")
            groups = []
            for group_data in groups_data:
                group = data.Group.parse_raw(group_data)
                groups.append(group)
            return groups
        else:
            print(f"Request Error {response.text}")
            return None
