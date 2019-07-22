"""
https://docs.microsoft.com/en-us/graph/api/directoryobject-get
"""

from py365 import auth, data
from ._base_resource import BaseResource


class DirectoryObjects(BaseResource):
    """

    """

    class DirectoryObject(BaseResource):
        pass

    def __init__(self, connection: auth.AppConnection):
        BaseResource.__init__(self, connection=connection, edgeBase='/directoryObjects')

    def getByIds(self) -> [data.DirectoryObject]:
        response = self.getAPI(edgeEnd="/getByIds")
        if response.ok:
            respData = response.json()
            dirObjectsData = respData.get("value")
            dirObjects = []
            for dirObjectData in dirObjectsData:
                dirObject = data.DirectoryObject()
                dirObject.fromResponse(data=dirObjectData)
                dirObjects.append(dirObject)
            return dirObjects
        else:
            print(f'Request Error{response.text}')
            return None
