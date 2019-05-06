from datetime import datetime

from .identity import Identity

from ._base_resource import BaseResource


class PlannerAssignment(BaseResource):

    def __init__(self):
        self.assignedBy: Identity
        self.assignedDateTime: datetime
        self.orderHint: str

        BaseResource.__init__(self)

    @classmethod
    def fromResponse(cls, retObj: object, data: dict):
        plannerAssignment = cls()
        BaseResource.fromResponse(retObj=plannerAssignment, data=data)

        return plannerAssignment
