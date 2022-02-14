"""
https://docs.microsoft.com/en-us/graph/api/directoryobject-get
"""

from py365 import auth, data
from ._base_resource import BaseResource


class DirectoryObjects(BaseResource):
    """ """

    class DirectoryObject(BaseResource):
        pass

    def __init__(self, connection: auth.AppConnection):
        BaseResource.__init__(
            self, connection=connection, edge_base="/directoryObjects"
        )

    def get_by_ids(self) -> [data.DirectoryObject]:
        response = self.__get_api__(edge_end="/get_by_ids")
        if response.ok:
            resp_data = response.json()
            dir_objects_data = resp_data.get("value")
            dir_objects = []
            for dir_object_data in dir_objects_data:
                dir_object = data.DirectoryObject.parse_raw(dir_object_data)
                dir_objects.append(dir_object)
            return dir_objects
        else:
            print(f"Request Error{response.text}")
            return None
