import requests
import json
from Task import Task

__author__ = "Adrián A. Fusco A."
__date__ = "24-09-2020"
__version__ = "0.1"


class Client:

    URL_LOGIN = 'index.php?c=access&a=login'
    URL_GET_TASKS = 'index.php?c=access&a=index'
    URL_BASE_TASK = 'index.php?c=task&a=view&id='

    HEADERS_CONTENT = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'charset': 'UTF-8'
    }

    # Part of the headers to get the tasks with filters:
    GET_UNTASKS_WITH_FILTERS_PAYLOAD = {
        # 0: pending, 1: completed
        'status': '0',
        'filter': 'assigned_to',
        'fval': '-1',
        # Group by 'Assigned to'
        'tasksGroupBy': 'nothing',
        # Order 'Created_on'
        'tasksOrderBy': 'created_on',
        'context': '{"1":[0,71],"2":[0]}',
        'currentdimension': '1',
        'ajax': 'true',
        'c': 'task',
        'a': 'get_tasks_groups_list',
        'current': 'tasks-panel'
    }

    def __init__(self: object, username: str, password: str, domain: str):
        self.domain = domain
        self.login_payload = {
            'login[username]': username,
            'login[password]': password
        }
        self.session = requests.Session()

    def __login(self: object):
        self.session.post(
            f"{self.domain}{self.URL_LOGIN}",
            data=self.login_payload
        )

    def __loadTasks(self: object):
        json_response = self.session.get(
            self.domain + self.URL_GET_TASKS,
            params=self.GET_UNTASKS_WITH_FILTERS_PAYLOAD,
            headers=self.HEADERS_CONTENT,
        )
        # Load the json response to parse the data:
        return json.loads(json_response.text)

    def __clearCookies(self: object):
        self.session.cookies.clear()

    def getTasks(self: object):
        self.__login()
        json_tasks = self.__loadTasks()
        self.__clearCookies()

        tasks = []
        if json_tasks['groups']:
            for task_information in json_tasks['groups'][0]['group_tasks']:
                task_url = self.domain + \
                           self.URL_BASE_TASK + \
                           str(task_information['id'])
                task_name = task_information['name']
                task = Task(task_name, task_url)
                tasks.append(task)
        return tasks
