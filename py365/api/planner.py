# API Reference
# https://docs.microsoft.com/en-us/graph/api/resources/planner-overview?view=graph-rest-1.0
from py365 import auth, rsc


class Planner(object):
    """
    You can use the Planner API in Microsoft Graph to create tasks and assign them to users in a group in Office 365.
    """

    class Plans(object):
        """
        Plans are the containers of tasks.
        To create a task in a plan, set the planId property on the task object to the ID of the plan
        while creating the task. Tasks currently cannot be created without plans.
        """

        def __init__(self, connection: auth.AppConnection, planID: str):
            self.connection: auth.AppConnection = connection
            self.planID = planID
            self.__PLAN_ENDPOINT = f'/planner/plans/{planID}'

        def listTasks(self):
            permissions = ["Group.Read.All", "Group.ReadWrite.All"]
            endpoint = self.__PLAN_ENDPOINT + '/tasks'
            response = self.connection.get(endpoint=endpoint, permissions=permissions)

            if response.ok:
                respJson = response.json()
                tasks = []
                for taskData in respJson:
                    task = rsc.PlannerTask.fromResponse(retObj=None, data=taskData)
                    tasks.append(task)
                return tasks
            else:
                print(f'Request Error{response.text}')
                return None

        def getPlannerPlan(self):
            permissions = ["Group.Read.All", "Group.ReadWrite.All"]
            endpoint = self.__PLAN_ENDPOINT
            response = self.connection.get(endpoint=endpoint, permissions=permissions)

            if response.ok:
                respJson = response.json()
                plans = []
                '''
                for planData in respJson:
                    plan = rsc.PlannerPlan.fromResponse(retObj=None, data=planData)
                    plan.append(plan)
                return plans
                '''
            else:
                print(f'Request Error{response.text}')
                return None

    def __init__(self, connection: auth.AppConnection):
        self.connection: auth.AppConnection = connection
        self.__PLANNER_ENDPOINT = '/planner/'

    def plans(self, planID) -> Plans:
        plansAPI = Planner.Plans(connection=self.connection, planID=planID)
        return plansAPI



