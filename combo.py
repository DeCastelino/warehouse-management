class Combo:

    def __init__(self, id, name, products_list, price, stock):
        self.ID = id
        self.name = name
        self.products_list = products_list
        self.price = price
        self.stock = stock

    def displayProduct (self):
        print('\n\t' + 'PRODUCT DETAILS')
        print('--------------------------------')
        print('ID: ' + self.ID)
        print('Name: ' + self.name)
        print('Products List:')
        for product in self.products_list:
            print(product.get_ID())
        print('Price: ' + str(self.price))
        print('--------------------------------')

    # getter methods
    def get_ID (self):
        return self.ID

    def get_name (self):
        return self.name

    def get_stock (self):
        return self.stock