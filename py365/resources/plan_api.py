from ._base_resource import BaseResource
from ._child_resource import ChildResource
from py365 import data


class PlanAPI(ChildResource):

    def __init__(self, plannerAPI: BaseResource, planID: str = None, plan: data.PlannerPlan = None):
        """
        Plans are the containers of tasks.
        To create a task in a plan, set the planId property on the task object to the ID of the plan
        while creating the task. Tasks currently cannot be created without plans.
        """
        if planID:
            self.planID = planID
        elif plan and plan.id:
            self.planID = plan.id
        else:
            raise ValueError("Either planID or plan must have valid value")
        super().__init__(baseAPI=plannerAPI, edgeMid=f"/plans/{self.planID}")

    def listTasks(self) -> [data.PlannerTask]:
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

    def listBuckets(self) -> [data.PlannerBucket]:
        buckets: [data.PlannerBucket] = []
        response = self.__getAPI__(edgeEnd="/buckets")
        if response.ok:
            respJson = response.json()
            for bucketData in respJson["value"]:
                bucket = data.PlannerBucket()
                bucket.fromResponse(data=bucketData)
                buckets.append(bucket)
        else:
            print(f'Request Error{response.text}')
        return buckets
