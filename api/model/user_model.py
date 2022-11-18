from api.model.address_model import AddressModel


class UserModel:
    id = int(),
    name = str()
    username = str()
    email = str()
    phone = str(),
    website = str(),
    company = {}

    def __init__(self, user_dic):
        self.id = user_dic.get('id')
        self.name = user_dic.get('name')
        self.username = user_dic.get('username')
        self.email = user_dic.get('email')
        self.address = AddressModel(user_dic.get('address'))
        self.phone = user_dic.get('phone')
        self.website = user_dic.get('website')
        self.company = user_dic.get('company')


    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_address(self):
        return self.address

    def to_dict(self):
        dictionary = self.__dict__
        dictionary["address"] = self.address.to_dict()
        return dictionary
