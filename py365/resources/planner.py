# API Reference
# https://docs.microsoft.com/en-us/graph/api/resources/planner-overview?view=graph-rest-1.0
from py365 import auth, data
from ._base_resource import BaseResource
from .bucket_api import BucketAPI
from .plan_api import PlanAPI


class Planner(BaseResource):
    """
    You can use the Planner API in Microsoft Graph to create tasks and assign them to users in a group in Office 365.
    """

    def __init__(self, connection: auth.AppConnection):
        super().__init__(connection, edgeBase='/planner')

    def plan(self, planID: str = None, plan: data.PlannerPlan = None) -> PlanAPI:
        plansAPI = PlanAPI(plannerAPI=self, planID=planID, plan=plan)
        return plansAPI

    def bucket(self, bucketID: str = None, bucket: data.PlannerBucket = None) -> BucketAPI:
        bucketAPI = BucketAPI(plannerAPI=self, bucketID=bucketID, bucket=bucket)
        return bucketAPI
