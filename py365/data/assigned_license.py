""" https://docs.microsoft.com/en-us/graph/api/resources/assignedlicense """

from typing import Optional, List

from pydantic import UUID4

from .base_data import BaseData


class AssignedLicense(BaseData):
    disabledPlans: Optional[List[UUID4]] = None
    skuId: Optional[UUID4] = None
