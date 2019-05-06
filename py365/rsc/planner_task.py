# Resource documentation:
# https://docs.microsoft.com/en-us/graph/api/resources/plannertask?view=graph-rest-1.0
from datetime import datetime

from .identity import Identity
from .planner_assignment import PlannerAssignment
from py365.utils import datetimeFromStr

from ._base_resource import BaseResource
from . import PlannerAppliedCategories


class PlannerTask(BaseResource):

    def __init__(self):
        self.activeChecklistItemCount: int = None
        self.appliedCategories: PlannerAppliedCategories = None
        self.assigneePriority: str = None
        self.assignments: [PlannerAssignment] = None
        self.bucketId: str = None
        self.checklistItemCount: int = None
        self.completedBy: [Identity] = []
        self.completedDateTime: datetime = None
        self.conversationThreadId: str = None
        self.createdBy: [Identity] = None
        self.createdDateTime: datetime = None
        self.dueDateTime: datetime = None
        self.hasDescription: bool = None
        self.id: str = None
        self.orderHint: str = None
        self.percentComplete: int = None
        self.planId: str = None
        # self.previewType: PreviewType
        self.referenceCount: int = None
        self.startDateTime: datetime = None
        self.title: str = None

        BaseResource.__init__(self)

    @classmethod
    def fromResponse(cls, retObj: object, data: dict):
        task = cls()
        task.activeChecklistItemCount = data.get("activeChecklistItemCount")
        task.appliedCategories = PlannerAppliedCategories.fromResponse(retObj=None, data=data)

        task.assigneePriority = data.get("assigneePriority")
        task.assignments = []
        for item in data.get("assignments"):
            task.assignments.append(PlannerAssignment.fromResponse(retObj=None, data=item))

        task.bucketId = data.get("bucketId")
        task.checklistItemCount = data.get("checklistItemCount")
        task.completedBy = []
        for item in data.get("completedBy"):
            task.completedBy.append(Identity.fromResponse(retObj=None, data=item))

        task.completedDateTime = datetimeFromStr(data.get("completedDateTime"))
        task.conversationThreadId = data
        task.createdBy = []
        for item in data.get("createdBy"):
            task.createdBy.append(Identity.fromResponse(retObj=None, data=item))

        task.createdDateTime = datetimeFromStr(data.get("createdDateTime"))
        task.dueDateTime = datetimeFromStr(data.get("dueDateTime"))
        task.hasDescription = data.get("hasDescription")
        task.id = data.get("id")
        task.orderHint = data.get("orderHint")
        task.percentComplete = data.get("percentComplete")
        task.planId = data.get("planId")
        # task.previewType
        task.referenceCount = data.get("referenceCount")
        task.startDateTime = datetimeFromStr(data.get("startDateTime"))
        task.title = data.get("title")

        return task
