from typing import Optional
from ._base_resource import BaseResource
from ._child_resource import ChildResource
from py365 import data


class BucketAPI(ChildResource):
    """
    https://docs.microsoft.com/en-us/graph/api/resources/plannerbucket?view=graph-rest-1.0

    The plannerBucket resource represents a bucket (or "custom column") for tasks in a plan in Office 365
    """

    def __init__(self, plannerAPI: BaseResource, bucketID: str = None, bucket: data.PlannerBucket = None):
        if bucketID:
            self.bucketID = bucketID
        elif bucket and bucket.id:
            self.bucketID = bucket.id
        else:
            self.bucketID = ""
        super().__init__(baseAPI=plannerAPI, edgeMid=f"/buckets/{self.bucketID}")

    def createBucket(self, newBucket: data.PlannerBucket) -> Optional[data.PlannerBucket]:
        """
        https://docs.microsoft.com/en-us/graph/api/planner-post-buckets?view=graph-rest-1.0&tabs=http

        Use this API to create a new plannerBucket
        :param newBucket: the new bucket data
        :type newBucket: data.PlannerBucket
        :return: the bucket object created
        :rtype: data.PlannerBucket
        """
        returnBucket = data.PlannerBucket()
        response = self.__postAPI__(postData=newBucket, returnData=returnBucket)
        if response.ok:
            return returnBucket
        else:
            print(f'Request Error {response.text}')
            return None

    def getBucket(self) -> Optional[data.PlannerBucket]:
        """
        https://docs.microsoft.com/en-us/graph/api/plannerbucket-get?view=graph-rest-1.0&tabs=http

        Retrieve the properties and relationships of plannerBucket object.
        :return: The requested bucket object
        :rtype: data.PlannerBucket
        """
        returnBucket = data.PlannerBucket()
        response = self.__getAPI__(returnData=returnBucket)
        if response.ok:
            return returnBucket
        else:
            print(f'Request Error {response.text}')
            return None

    def listTasks(self) -> [data.PlannerTask]:
        """
        https://docs.microsoft.com/en-us/graph/api/plannerbucket-list-tasks?view=graph-rest-1.0&tabs=http

        Retrieve a list of plannerTask objects associated to a plannerBucket object
        :return: list of tasks
        :rtype: [data.PlannerTask]
        """
        tasks: [data.PlannerTask] = []
        response = self.__getAPI__(edgeEnd="/tasks")
        if response.ok:
            respJson = response.json()
            for taskData in respJson["value"]:
                task = data.PlannerTask()
                task.fromResponse(data=taskData)
                tasks.append(task)
        else:
            print(f'Request Error{response.text}')
        return tasks

    def updateBucket(self, updateBucket: data.PlannerBucket) -> Optional[data.PlannerBucket]:
        """
        https://docs.microsoft.com/en-us/graph/api/plannerbucket-update?view=graph-rest-1.0&tabs=http

        Update the properties of plannerBucket object
        :param updateBucket: the information to update
        :type updateBucket: data.PlannerBucket
        :return: the updated bucket object data
        :rtype: data.PlannerBucket
        """
        returnBucket = data.PlannerBucket()
        response = self.__patchAPI__(patchData=updateBucket, returnData=returnBucket)
        if response.ok:
            return returnBucket
        else:
            print(f'Request Error {response.text}')
            return None

    def deleteBucket(self, deleteBucket: data.PlannerBucket):
        """
        https://docs.microsoft.com/en-us/graph/api/plannerbucket-delete?view=graph-rest-1.0&tabs=http

        Delete plannerBucket
        :return: none
        :rtype: none
        """
        response = self.__deleteAPI__(deleteData=deleteBucket)
        if not response.ok:
            print(f'Request Error {response.text}')
