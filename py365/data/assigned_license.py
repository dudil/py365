""" https://docs.microsoft.com/en-us/graph/api/resources/assignedlicense """

from typing import Optional, List
from pydantic import BaseModel, UUID4


class AssignedLicense(BaseModel):
    disabledPlans: Optional[List[UUID4]] = None
    skuId: Optional[UUID4] = None
