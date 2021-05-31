class Order:
    customer = None
    product = None
    quantity = None
    time = None
    comment = None

    # creating order
    def __init__ (self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity

    def displayOrder (self):
        print('\n\t' + 'ORDER DETAILS')
        print('--------------------------------')
        print('Customer Name: ' + self.customer.get_name())
        print('Product ID: ' + self.product.get_ID())
        print('Time: ' + self.time)
        print('Comment: ' + self.comment)
        print('--------------------------------')

    # setter methods
    def set_time (self, time):
        self.time = time

    def set_comment (self, comment):
        self.comment = comment

    # getter methods
    def get_customer_ID(self):
        return self.customer_ID

    def get_product_ID(self):
        return self.product_ID

    def get_quantity(self):
        return self.quantity

    def get_time (self):
        return self.time

    def get_time (self):
        return self.time

    def get_comment (self):
        return self.comment