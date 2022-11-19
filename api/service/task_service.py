from api.dao.task_dao import TaskDao
from flask import abort


class TaskService:
    taskDao = TaskDao()

    def get_tasks(self, completed=None, title=''):
        if title is None:
            title = ''
        if completed is not None:
            if completed.lower() == 'true':
                completed = True
            elif completed.lower() == 'false':
                completed = False
        tasks = self.taskDao.get_tasks(completed=completed, title=title)
        tasks_as_dic = list(map(lambda x: x.to_dict(), tasks))
        to_return = {"total_items": len(tasks_as_dic),
                     "data": tasks_as_dic}
        return to_return, 200

    def get_task_by_id(self, task_id):
        if not task_id.isnumeric():
            abort(404)
        task = self.taskDao.get_task_by_id(task_id)
        if not task:
            abort(404)
        task_as_dic = task[0].to_dict()
        return task_as_dic, 200
    
    def get_task_by_user_id(self, user_id, completed, title):
        if title is None:
            title = ''
        if completed is not None:
            if completed.lower() == 'true':
                completed = True
            elif completed.lower() == 'false':
                completed = False
        tasks = self.taskDao.get_task_by_user_id(user_id, completed=completed, title=title)
        tasks = list(map(lambda x: x.to_dict(), tasks))
        to_return = {"total_items": len(tasks),
                     "data": tasks}
        return to_return, 200
