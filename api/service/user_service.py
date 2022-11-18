class UserService:

    def get_users(self):
        return "users"

    def get_users_by_id(self, user_id):
        return "user: " + user_id

    def get_tasks_of_user(self, user_id):
        return "tasks of user: " + user_id

    def get_task_by_id_of_user(self, user_id, tid):
        return "task:" + tid + "of user: " + user_id
