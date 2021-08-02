# Resource documentation
# https://docs.microsoft.com/en-us/graph/api/resources/identity?view=graph-rest-1.0
from pydantic import BaseModel
from py365.utils import OptStr


class Identity(BaseModel):
    displayName: OptStr = None
    id: OptStr = None
