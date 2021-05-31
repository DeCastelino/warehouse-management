
from customer import Customer

class RetailCustomer(Customer):
    
    discount_rate = None

    # this constructor will be called when user does not specify discount rate
    def __init__(self, ID, name, price):
        super().__init__(ID, name)
        self.discount_rate = 10
        self.price = price

    # creating new customer while ordering
    def __init__(self, ID, name):
        super().__init__(ID, name)
        self.discount_rate = None
        self.price = None

    # constructor with id and name as parameters
    def __init__(self, ID, name, discount_rate, price):
        super().__init__(ID, name)
        self.discount_rate = discount_rate
        self.price = price

    def get_discount(self, price):
        return price - ((self.discount_rate / 100) * price)

    def displayCustomer(self):
        
        print('\n\t' + 'CUSTOMER DETAILS')
        print('--------------------------------')
        print('ID: \t' + str(self.ID))
        print('Name: ' + self.name)
        print('Discount Rate: ' + str(self.discount_rate))
        print('Total Price: ' + str(self.price))
        print('Type: Retailer')
        print('--------------------------------')

    def setRate(self, new_rate):
        self.discount_rate = new_rate

    # getter methods
    def get_discount_rate(self):
        return self.discount_rate

    def get_name(self):
        return self.name