import json

from api.model.user_model import UserModel


class UserDao:
    def __init__(self):
        f = open('./api/dao/users.json')
        self.users = json.load(f)
        f.close()
        self.users = list(map(lambda x: UserModel(x), self.users))

    def get_users(self):
        return self.users

    def get_user_by_id(self, uid):
        return list(filter(lambda x: x.get_id() == uid, self.users))
