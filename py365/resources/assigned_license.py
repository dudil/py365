""" https://docs.microsoft.com/en-us/graph/api/resources/assignedlicense """
import uuid

from ._base_resource import BaseResource


class AssignedLicense(BaseResource):
    """
    Represents a license assigned to a user.
    The assignedLicenses property of the user entity is a collection of assignedLicense.
    :param disabledPlans: A collection of the unique identifiers for plans that have been disabled
    :param skuId: The unique identifier for the SKU
    """

    def __init__( self, disabledPlans: [uuid.UUID], skuId: uuid.UUID ):
        self.disabledPlans: [uuid.UUID] = disabledPlans
        self.skuId: uuid.UUID = skuId
        BaseResource.__init__(self)
