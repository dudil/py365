from datetime import datetime

from .base_data import BaseData
from .identity import Identity


class PlannerAssignment(BaseData):
    assignedBy: Identity = None
    assignedDateTime: datetime = None
    orderHint: str = None

    """
    @classmethod
    def fromResponse(cls, retObj: object, data: dict):
        plannerAssignment = cls()
        BaseData.fromResponse(retObj=plannerAssignment, data=data)

        return plannerAssignment
    """
