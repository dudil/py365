# Resource documentation:
# https://docs.microsoft.com/en-us/graph/api/resources/plannertask?view=graph-rest-1.0
import attr
from datetime import datetime

from . import PlannerAppliedCategories
from .base_data import BaseData
from .identity import Identity
from .planner_assignment import PlannerAssignment


@attr.s(auto_attribs=True)
class PlannerTask(BaseData):
    activeChecklistItemCount: int = None
    appliedCategories: PlannerAppliedCategories = None
    assigneePriority: str = None
    assignments: [PlannerAssignment] = None
    bucketId: str = None
    checklistItemCount: int = None
    completedBy: [Identity] = None
    completedDateTime: datetime = None
    conversationThreadId: str = None
    createdBy: [Identity] = None
    createdDateTime: datetime = None
    dueDateTime: datetime = None
    hasDescription: bool = None
    id: str = None
    orderHint: str = None
    percentComplete: int = None
    planId: str = None
    # previewType: PreviewType
    referenceCount: int = None
    startDateTime: datetime = None
    title: str = None

    """
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
    """
