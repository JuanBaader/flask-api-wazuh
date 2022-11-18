from flask import abort

from api.dao.user_dao import UserDao
from api.service.task_service import TaskService


class UserService:
    user_dao = UserDao()
    task_service = TaskService()

    def get_users(self):
        return list(map(lambda x: x.to_dict(), self.user_dao.get_users()))

    def get_users_by_id(self, user_id):
        if not user_id.isnumeric():
            abort(404)
        user = self.user_dao.get_user_by_id(int(user_id))
        if not user:
            abort(404)
        user = user[0].to_dict()
        return user

    def get_tasks_of_user(self, user_id):
        user = self.get_users_by_id(user_id)
        return "tasks of user: " + user_id

    def get_task_by_id_of_user(self, user_id, tid):
        return "task:" + tid + "of user: " + user_id
