
class Customer:
    ID = None
    name = None
    price = None

    # constructor with Id and name as parameters
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name

    def get_discount(self, price):
        pass

    # getter methods
    def get_ID(self):
        return self.ID

    def get_name(self):
        return self.name