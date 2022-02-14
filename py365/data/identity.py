# Resource documentation
# https://docs.microsoft.com/en-us/graph/api/resources/identity?view=graph-rest-1.0
from py365.utils import OptStr
from .base_data import BaseData


class Identity(BaseData):
    displayName: OptStr = None
    id: OptStr = None
