# Resource document
# https://docs.microsoft.com/en-us/graph/api/resources/plannerbucket?view=graph-rest-1.0

from .base_data import BaseData


class PlannerBucket(BaseData):
    id: str = None
    name: str = None
    orderHint: str = None
    planId: str = None
