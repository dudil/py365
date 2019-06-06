# Resource documentation
# https://docs.microsoft.com/en-us/graph/api/resources/identity?view=graph-rest-1.0
import attr
from ._base_data import BaseData


@attr.s(auto_attribs=True)
class Identity(BaseData):
    displayName: str = None
    id: str = None
