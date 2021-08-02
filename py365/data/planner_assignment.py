from pydantic import BaseModel
from datetime import datetime


from .identity import Identity


class PlannerAssignment(BaseModel):
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
