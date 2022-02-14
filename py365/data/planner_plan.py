"""
https://docs.microsoft.com/en-us/graph/api/resources/plannerplan
"""
import datetime
from typing import Optional

from .base_data import BaseData
from .identity_set import IdentitySet


class PlannerPlan(BaseData):
    """
    The plannerPlan resource represents a plan in Office 365.
    A plan can be owned by a group and contains a collection of plannerTasks.
    It can also have a collection of plannerBuckets.
    Each plan object has a details object that can contain more information about the plan.
    For more information about the relationships between groups, plans, and tasks, see Planner.
    """

    createdDateTime: datetime = None
    id: Optional[str] = None
    owner: Optional[str] = None
    title: Optional[str] = None
    createdBy: Optional[IdentitySet] = None
