import json
import os
from api.model.task_model import TaskModel


class TaskDao:
    def __init__(self):
        f = open('./api/dao/tasks.json')
        self.tasks = json.load(f)
        f.close()
        self.tasks = list(map(lambda x: TaskModel(x), self.tasks))

    def get_tasks(self, completed=None, title=''):
        filtered = self.tasks
        if completed is not None:
            filtered = list(filter(lambda x: x.get_completed() == completed, filtered))
        filtered = list(filter(lambda x: title in x.get_title(), filtered))
        return filtered

    def get_task_by_id(self, task_id):
        return list(filter(lambda x: x.get_id() == task_id, self.tasks))

    def get_task_by_user_id(self, user_id, completed=None, title=''):
        return list(filter(lambda
                               x: ((x.get_user_id() == user_id) and (title in x.get_title()) and
                                   (True if completed is None else x.get_completed() == completed)),
                           self.tasks))
