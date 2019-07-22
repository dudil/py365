# API Reference
# https://docs.microsoft.com/en-us/graph/api/resources/planner-overview?view=graph-rest-1.0
from typing import Optional
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

    def plans(self, planID: str = None, plan: data.PlannerPlan = None) -> PlanAPI:
        plansAPI = PlanAPI(plannerAPI=self, planID=planID, plan=plan)
        return plansAPI

    def bucket(self, bucketID: str = None, bucket: data.PlannerBucket = None) -> BucketAPI:
        bucketAPI = BucketAPI(plannerAPI=self, bucketID=bucketID, bucket=bucket)
        return bucketAPI

    def createBucket(self, bucket: data.PlannerBucket) -> Optional[data.PlannerBucket]:
        """
        https://docs.microsoft.com/en-us/graph/api/planner-post-buckets?view=graph-rest-1.0&tabs=http
        :param bucket:
        :type bucket:
        :return:
        :rtype:
        """
        json = bucket.json
        response = self.postAPI("/buckets", json=json)
        if response.ok:
            respJson = response.json()
            bucket = data.PlannerBucket()
            bucket.fromResponse(data=respJson)
            return bucket
        else:
            print(f'Request Error{response.text}')
            return None
