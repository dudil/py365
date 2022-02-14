from typing import Optional

from .base_data import BaseData


class DirectoryObject(BaseData):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/directoryobject?view=graph-rest-1.0

    Represents an Azure Active Directory object.
    The directoryObject type is the base type for many other directory entity types.
    """

    id: Optional[str] = None

    @property
    def odata_id(self) -> str:
        return f"https://graph.microsoft.com/v1.0/directoryObjects/{self.id}"
