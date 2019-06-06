""" https://docs.microsoft.com/en-us/graph/api/resources/assignedlicense """
import uuid
import attr

from ._base_data import BaseData


@attr.s(auto_attribs=True)
class AssignedLicense(BaseData):
    disabledPlans: [uuid.UUID] = None
    skuId: uuid.UUID = None
