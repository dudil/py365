import attr
from .base_data import BaseData


@attr.s(auto_attribs=True)
class DirectoryObject(BaseData):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/directoryobject?view=graph-rest-1.0

    Represents an Azure Active Directory object.
    The directoryObject type is the base type for many other directory entity types.
    """

    id: str = None

    @property
    def odata_id(self) -> str:
        return f"https://graph.microsoft.com/v1.0/directoryObjects/{self.id}"
