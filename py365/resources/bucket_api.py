from ._base_resource import BaseResource
from ._child_resource import ChildResource
from py365 import data


class BucketAPI(ChildResource):

    def __init__(self, plannerAPI: BaseResource, bucketID: str = None, bucket: data.PlannerBucket = None):
        if bucketID:
            self.bucketID = bucketID
        elif bucket and bucket.id:
            self.bucketID = bucket.id
        else:
            raise ValueError("Either bucketId or bucket must have a valid value")
        super().__init__(baseAPI=plannerAPI, edgeMid=f"/buckets/{self.bucketID}")

    def listTasks(self) -> [data.PlannerTask]:
        tasks: [data.PlannerTask] = []
        response = self.getAPI(edgeEnd="/tasks")
        if response.ok:
            respJson = response.json()
            for taskData in respJson["value"]:
                task = data.PlannerTask()
                task.fromResponse(data=taskData)
                tasks.append(task)
        else:
            print(f'Request Error{response.text}')
        return tasks
