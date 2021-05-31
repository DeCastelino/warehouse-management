class Product:
    ID = None
    name = None
    price = None
    stock = None

    def __init__(self, ID, name, price, stock):
        self.ID = ID
        self.name = name
        self.price = price
        self.stock = stock

    def set_price(self, new_price):
        self.price = new_price

    def set_stock(self, new_stock):
        self.stock = new_stock

    def displayProduct(self):
        print('\n\t' + 'PRODUCT DETAILS')
        print('--------------------------------')
        print('ID: \t' + self.ID)
        print('Name: ' + self.name)
        print('Price: ' + str(self.price))
        print('Stock: ' + str(self.stock))
        print('--------------------------------')

    # getter methods
    def get_ID (self):
        return self.ID

    def get_name(self):
        return self.name

    def get_stock (self):
        return self.stock

    def get_price (self):
        return self.price