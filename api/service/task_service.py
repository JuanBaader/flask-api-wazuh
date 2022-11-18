from api.dao.task_dao import TaskDao


class TaskService:
    taskDao = TaskDao()

    def get_tasks(self, completed=None, title=''):
        if title is None:
            title = ''
        if completed.lower() == 'true':
            completed = True
        elif completed.lower() == 'false':
            completed = False
        return self.taskDao.get_tasks(completed=completed, title=title)

    def get_task_by_id(self, tid):
        return self.taskDao.get_task_by_id(tid)
