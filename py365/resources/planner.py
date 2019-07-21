# API Reference
# https://docs.microsoft.com/en-us/graph/api/resources/planner-overview?view=graph-rest-1.0
from py365 import auth, data
from ._base_resource import BaseResource


class Planner(BaseResource):
    """
    You can use the Planner API in Microsoft Graph to create tasks and assign them to users in a group in Office 365.
    """

    class Plans(BaseResource):
        """
        Plans are the containers of tasks.
        To create a task in a plan, set the planId property on the task object to the ID of the plan
        while creating the task. Tasks currently cannot be created without plans.
        """

        def __init__(self, connection: auth.AppConnection, planID: str):
            self.planID = planID
            BaseResource.__init__(self, connection, f'/planner/plans/{planID}')

        def listTasks(self) -> [data.PlannerTask]:
            permissions = ["Group.Read.All", "Group.ReadWrite.All"]
            endpoint = self.ENDPOINT + '/tasks'
            response = self.connection.get(endpoint=endpoint, permissions=permissions)

            tasks: [data.PlannerTask] = []

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
            endpoint = self.ENDPOINT + '/buckets'
            response = self.connection.get(endpoint=endpoint)

            buckets: [data.PlannerBucket] = []

            if response.ok:
                respJson = response.json()
                for bucketData in respJson["value"]:
                    bucket = data.PlannerBucket()
                    bucket.fromResponse(data=bucketData)
                    buckets.append(bucket)
            else:
                print(f'Request Error{response.text}')

            return buckets

    def __init__(self, connection: auth.AppConnection):
        BaseResource.__init__(self, connection, '/planner/')

    def plans(self, planID) -> Plans:
        plansAPI = Planner.Plans(connection=self.connection, planID=planID)
        return plansAPI
