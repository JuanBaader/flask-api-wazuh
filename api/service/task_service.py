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
        return to_return

    def get_task_by_id(self, tid):
        task = self.taskDao.get_task_by_id(tid)
        if not task:
            abort(404)
        task_as_dic = task[0].to_dict()
        return task_as_dic, 200
