"""
https://docs.microsoft.com/en-us/graph/api/resources/plannerplan
"""
from ._base_data import BaseData
from .identity_set import IdentitySet
import attr
import datetime


@attr.s(auto_attribs=True)
class PlannerPlan(BaseData):
    """
    The plannerPlan resource represents a plan in Office 365.
    A plan can be owned by a group and contains a collection of plannerTasks.
    It can also have a collection of plannerBuckets.
    Each plan object has a details object that can contain more information about the plan.
    For more information about the relationships between groups, plans, and tasks, see Planner.
    """

    createdDateTime: datetime = None
    id: str = None
    owner: str = None
    title: str = None
    createdBy: IdentitySet = None
