
from customer import Customer

class WholesaleCustomer(Customer):

    amount_threshold = None
    price = None
    first_rate = None
    second_rate = None

    # contructor if the rate is mentioned
    def __init__(self, ID, name, first_rate, price):
        super().__init__(ID, name)
        self.amount_threshold = 1000  # default will be $1000
        self.price = price
        self.first_rate = first_rate
        self.second_rate = first_rate + 5


    def get_discount(self, price):
        if price > self.amount_threshold:
            return price - ((self.second_rate / 100) * price)
        else:
            return price - ((self.first_rate / 100) * price)

    def displayCustomer(self):
        print('\n\t' + 'CUSTOMER DETAILS')
        print('--------------------------------')
        print('ID: \t' + str(self.ID))
        print('Name: ' + self.name)
        print('Amount Threshold: ' + str(self.amount_threshold))
        print('First Rate of Discount: ' + str(self.first_rate))
        print('Second Rate of Discount: ' + str(self.second_rate))
        print('Total Price: ' + str(self.price))
        print('Type: Wholesaler')
        print('--------------------------------')

    # setter methods
    def setRate(self, first_rate):
        self.first_rate = first_rate
        self.second_rate = first_rate + 5

    def set_amount_threshold (self, amount):
        self.amount_threshold = amount

    # getter methods
    def get_ID(self):
        return self.ID

    def get_name(self):
        return self.name

    def get_amount_threshold(self):
        return self.amount_threshold

    def get_first_rate(self):
        return self.first_rate

    def get_second_rate(self):
        return self.second_rate