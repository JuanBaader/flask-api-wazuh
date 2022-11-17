class TaskService:
    def get_tasks(self, completed=None, title=''):
        response = "task"
        if (completed != None):
            response = response + " completed?=" + completed
        response += "title?" + title
        return response

    def get_task_by_id(self, user_id):
        return "task" + user_id
