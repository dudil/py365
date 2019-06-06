import attr
from datetime import datetime

from ._base_data import BaseData
from .identity import Identity


@attr.s(auto_attribs=True)
class PlannerAssignment(BaseData):
    assignedBy: Identity = None
    assignedDateTime: datetime = None
    orderHint: str = None

    '''
    @classmethod
    def fromResponse(cls, retObj: object, data: dict):
        plannerAssignment = cls()
        BaseData.fromResponse(retObj=plannerAssignment, data=data)

        return plannerAssignment
    '''
