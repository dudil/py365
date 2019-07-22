# Resource document
# https://docs.microsoft.com/en-us/graph/api/resources/plannerbucket?view=graph-rest-1.0

import attr

from ._base_data import BaseData


@attr.s(auto_attribs=True)
class PlannerBucket(BaseData):
    id: str = None
    name: str = None
    orderHint: str = None
    planId: str = None
