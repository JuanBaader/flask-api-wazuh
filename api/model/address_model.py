class AddressModel:
    street = str()
    suite = str()
    city = str()
    zipcode = str()
    geo = {}

    def __init__(self, address_dict):
        self.street = address_dict.get('street')
        self.suite = address_dict.get('suite')
        self.city = address_dict.get('city')
        self.zipcode = address_dict.get('zipcode')
        self.geo = address_dict.get('geo')

    def get_street(self):
        return self.street

    def get_suite(self):
        return self.suite

    def get_city(self):
        return self.city

    def get_zipcode(self):
        return self.zipcode

    def get_geo(self):
        return self.geo

    def to_dict(self):
        return self.__dict__
