import json


class TaskModel:
    user_id = int()
    id = int()
    title = str()
    completed = bool()

    def __init__(self, task_dic):
        self.user_id = task_dic.get('user_id')
        self.id = task_dic.get('id')
        self.title = task_dic.get('title')
        self.completed = task_dic.get('completed')

    def get_user_id(self):
        return self.user_id

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_completed(self):
        return self.completed

    def __str__(self):
        return self.to_json()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)

    def to_dict(self):
        return self.__dict__
