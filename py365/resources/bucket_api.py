from typing import Optional

from py365 import data
from ._base_resource import BaseResource
from ._child_resource import ChildResource


class BucketAPI(ChildResource):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/plannerbucket?view=graph-rest-1.0

    The plannerBucket resource represents a bucket (or "custom column") for tasks in a plan in Office 365
    """

    def __init__(
        self,
        plannerAPI: BaseResource,
        bucketID: str = None,
        bucket: data.PlannerBucket = None,
    ):
        if bucketID:
            self.bucketID = bucketID
        elif bucket and bucket.id:
            self.bucketID = bucket.id
        else:
            self.bucketID = ""
        super().__init__(base_api=plannerAPI, edge_mid=f"/buckets/{self.bucketID}")

    def create_bucket(
        self, newBucket: data.PlannerBucket
    ) -> Optional[data.PlannerBucket]:
        """
        https://docs.microsoft.com/en-us/graph/api/planner-post-buckets?view=graph-rest-1.0&tabs=http

        Use this API to create a new plannerBucket
        :param newBucket: the new bucket data
        :type newBucket: data.PlannerBucket
        :return: the bucket object created
        :rtype: data.PlannerBucket
        """
        return_bucket = data.PlannerBucket()
        response = self.__post_api__(post_data=newBucket, return_data=return_bucket)
        if response.ok:
            return return_bucket
        else:
            print(f"Request Error {response.text}")
            return None

    def get_bucket(self) -> Optional[data.PlannerBucket]:
        """
        https://docs.microsoft.com/en-us/graph/api/plannerbucket-get?view=graph-rest-1.0&tabs=http

        Retrieve the properties and relationships of plannerBucket object.
        :return: The requested bucket object
        :rtype: data.PlannerBucket
        """
        return_bucket = data.PlannerBucket()
        response = self.__get_api__(return_data=return_bucket)
        if response.ok:
            return return_bucket
        else:
            print(f"Request Error {response.text}")
            return None

    def list_tasks(self) -> [data.PlannerTask]:
        """
        https://docs.microsoft.com/en-us/graph/api/plannerbucket-list-tasks?view=graph-rest-1.0&tabs=http

        Retrieve a list of plannerTask objects associated to a plannerBucket object
        :return: list of tasks
        :rtype: [data.PlannerTask]
        """
        tasks: [data.PlannerTask] = []
        response = self.__get_api__(edge_end="/tasks")
        if response.ok:
            resp_json = response.json()
            for task_data in resp_json["value"]:
                task = data.PlannerTask()
                task.parse_obj(obj=task_data)
                tasks.append(task)
        else:
            print(f"Request Error{response.text}")
        return tasks

    def update_bucket(
        self, updateBucket: data.PlannerBucket
    ) -> Optional[data.PlannerBucket]:
        """
        https://docs.microsoft.com/en-us/graph/api/plannerbucket-update?view=graph-rest-1.0&tabs=http

        Update the properties of plannerBucket object
        :param updateBucket: the information to update
        :type updateBucket: data.PlannerBucket
        :return: the updated bucket object data
        :rtype: data.PlannerBucket
        """
        return_bucket = data.PlannerBucket()
        response = self.__patch_api__(
            patch_data=updateBucket, return_data=return_bucket
        )
        if response.ok:
            return return_bucket
        else:
            print(f"Request Error {response.text}")
            return None

    def delete_bucket(self, deleteBucket: data.PlannerBucket):
        """
        https://docs.microsoft.com/en-us/graph/api/plannerbucket-delete?view=graph-rest-1.0&tabs=http

        Delete plannerBucket
        :return: none
        :rtype: none
        """
        response = self.__delete_api__(delete_data=deleteBucket)
        if not response.ok:
            print(f"Request Error {response.text}")
