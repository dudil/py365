# Resource documentation:
# https://docs.microsoft.com/en-us/graph/api/resources/plannerappliedcategories?view=graph-rest-1.0
from ._base_resource import BaseResource


class PlannerAppliedCategories(BaseResource):
    """
    The AppliedCategoriesCollection resource represents the collection of categories (or labels)
    that have been applied to a task. It is part of the plannerTask object.
    There can be up to 6 categories applied to a task. Category descriptions, e.g. category1, category2 etc.,
    are part of the plan details object. This is an open type.
    """

    def __init__(self):
        self.category1: bool = False
        self.category2: bool = False
        self.category3: bool = False
        self.category4: bool = False
        self.category5: bool = False
        self.category6: bool = False
        BaseResource.__init__(self)

    @classmethod
    def fromResponse(cls, retObj: object, data: dict):
        plannerAppliedCategories = cls()
        plannerAppliedCategories.category1 = data.get("category1", False)
        plannerAppliedCategories.category2 = data.get("category2", False)
        plannerAppliedCategories.category3 = data.get("category3", False)
        plannerAppliedCategories.category4 = data.get("category4", False)
        plannerAppliedCategories.category5 = data.get("category5", False)
        plannerAppliedCategories.category6 = data.get("category6", False)

        return plannerAppliedCategories

    @property
    def payload(self) -> dict:
        """
        convert the resource into payload for the Open Graph365 API call
        Special case here since only True should be included in the payload
        """
        data = vars(self)
        payload: dict = {}
        for key, val in data.items():
            if val is True:
                payload.update({key: val})

        return payload
