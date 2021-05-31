
from retailCustomer import RetailCustomer
from wholesaleCustomer import WholesaleCustomer
from product import Product
from order import Order
from combo import Combo

class Records:
    cust_dict = {}
    prod_dict = {}
    order_dict = {}

    def readCustomers(self):
        try:
            # read data from customers.txt
            f = open('customers.txt', 'r')
            row = f.readline()
            # read each line from the file
            while row:
                tokens = row.strip().split(',')
                id = int(tokens[0].strip())
                name = tokens[1].strip()
                cust_type = tokens[2].strip()
                discount = float(tokens[3].strip())
                price = float(tokens[4].strip())

                row = f.readline()

                # create objects from these local variables
                if cust_type.upper() == 'R':
                    customer = RetailCustomer(id, name, discount, price)
                else:
                    customer = WholesaleCustomer(id, name, discount, price)

                # adding customer object to dictionary
                self.cust_dict[id] = customer

            f.close()
            return self.cust_dict
        except (FileNotFoundError, IOError):
            print('customers.txt file not found')
            quit()

    def readProducts(self):
        try:
            # read data from products.txt
            f = open('products.txt', 'r')
            row = f.readline()
            # read each line from the file
            while row:
                tokens = row.strip().split(',')
                id = tokens[0].strip()
                name = tokens[1].strip()
                if 'P' in id:
                    price = float(tokens[2].strip())
                    stock = int(tokens[3].strip())

                    # create objects from these local variables
                    product = Product(id, name, price, stock)

                    # adding product object to dictionary
                    self.prod_dict[id] = product
                else:
                    # reading Combo products from file
                    products_list = []
                    quantity = None
                    price = 0
                    for i in range(2, len(tokens)):
                        if 'P' in tokens[i]:
                            prod_id = tokens[i].strip()
                            products_list.append(self.prod_dict[prod_id])
                            price += self.prod_dict[prod_id].get_price()
                        else:
                             quantity = int(tokens[i].strip())
                    price = price * 0.9
                    # creating objects from these local variables
                    combo = Combo(id, name, products_list, price, quantity)

                    # adding combo object to dictionary
                    self.prod_dict[id] = combo
                row = f.readline()

            f.close()
            return self.prod_dict
        except (FileNotFoundError, IOError):
            print('products.txt file is missing')
            quit()

    #reading orders
    def readOrders (self):
        f = open('orders.txt', 'r')
        row = f.readline()
        while row:
            tokens = row.strip().split(',')
            customer_info = tokens[0]
            product_info = tokens[1]
            quantity = tokens[2]

            # finding customer object
            if customer_info in self.cust_dict.keys():
                customer = self.cust_dict[customer_info]
            else:
                for cust_ID in self.cust_dict:
                    if self.cust_dict[cust_ID].get_name() == customer_info:
                        customer = self.cust_dict[cust_ID]
            
            # finding product object
            if product_info in self.prod_dict.keys():
                product = self.prod_dict[product_info]
            else:
                for prod_ID in self.prod_dict:
                    if self.prod_dict[prod_ID].get_name() == product_info:
                        product = self.prod_dict[prod_ID]

            # creating Order object from above variables
            order = Order(customer, product, quantity)
            # adding orders created to dictionary
            self.order_dict[customer.get_ID()] = order

            for i in range(3, len(tokens)):
                if '-' in tokens[i]:
                    # It is a date
                    date = tokens[i]
                    order.set_time(date)
                else:
                    # It is a comment
                    comment = tokens[i]
                    order.set_comment(comment)
        return self.order_dict
            


    # find if a customer exists or not (search by ID or name)
    def findCustomer(self, find_value):
        for key in self.cust_dict:
            if find_value == key or find_value == self.cust_dict[key].get_name():
                return self.cust_dict[key]
            else:
                return None

    # find if a product exists or not (search by ID or name)
    def findProduct(self, find_value):
        for key in self.prod_dict:
            if find_value == key or find_value == self.prod_dict[key].get_name():
                return self.prod_dict[key]
            else:
                return None

    def listCustomers(self):
        for key in self.cust_dict:
            self.cust_dict[key].displayCustomer()

    def listProducts(self):
        for key in self.prod_dict:
            self.prod_dict[key].displayProduct()

    def listOrders (self):
        for key in self.order_dict:
            self.order_dict[key].displayOrder()

    # adding new customer to dictionary
    def add_customer (self, customer):
        self.cust_dict[customer.get_ID()] = customer

    # adding new product to dictionary
    def add_Product (self, product):
        self.prod_dict[product.get_ID()] = product