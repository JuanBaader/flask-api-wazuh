import json
import os

class TaskDao:
    def __init__(self):
        f = open('./api/dao/tasks.json')
        self.tasks = json.load(f)
        f.close()

    def get_tasks(self, completed=None, title=''):
        filtered = self.tasks
        if completed is not None:
            filtered = list(filter(lambda x: x.get('completed') == completed, filtered))
        filtered = list(filter(lambda x: title in x.get('title'), filtered))
        return filtered

    def get_task_by_id(self, tid):
        return list(filter(lambda x: x.get('id') == tid, self.tasks))
