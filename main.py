
from records import Records
from retailCustomer import RetailCustomer
from wholesaleCustomer import WholesaleCustomer
from order import Order
from exceptions import *
import datetime

#---------------------------------------------------------
#-------------   Credit Level Completed   ----------------
#-------------    working on DI level     ----------------
#---------------------------------------------------------

class Operations:

    def __init__(self):

        records = Records()
        cust_records = records.readCustomers()
        prod_records = records.readProducts()

        # MENU
        while (True):
            try:
                print('\n')
                print('--------------------------------')
                print('              MENU              ')
                print('--------------------------------')
                print('1. Display all customers')
                print('2. Display all products')
                print('3. Order a product')
                print('4. Get a product\'s details')
                print('5. Adjust customer\'s discount rate')
                print('6. Adjust customer\'s amount threshold')
                print('7. Display all orders')
                print('0. Quit')
                print('--------------------------------')
                print('\n')

                value = int(input('Enter your option (0 - 4): '))

                if value == 0:
                    quit()

                # displaying all customers
                elif value == 1:
                    records.listCustomers()

                # displaying all products
                elif value == 2:
                    records.listProducts()

                # creating order
                elif value == 3:
                    #reading orders.txt
                    order_records = records.readOrders()
                    try:
                        try:
                            cust_id = int(input('Enter the customer ID: '))
                            if cust_id not in cust_records.keys():
                                raise NewCustomerException
                        except NewCustomerException:
                            response = input('Seems like there is no such customer with this customer ID. Want to create one? (Y/n): ')
                            if 'Y' in response.upper():
                                name = input('Enter new customer\'s name: ')
                                cust_type = input('Type of Customer (R)etail or (W)holesale: ' )
                                if 'R' in cust_type.upper():
                                    print('ID: ' + str(cust_id))
                                    print('Creating Retail customer')
                                    customer = RetailCustomer(cust_id, name)
                                    print('Created')
                                else:
                                    print('Creating Wholesale customer')
                                    customer = WholesaleCustomer(cust_id, name)
                                    print('Created')
                                cust_records[cust_id] = customer
                                # addign in records class as well
                                records.add_customer(customer)
                                continue

                        while(True):
                            try:
                                prod_id = input('Enter product ID: ')
                                if prod_id.upper() not in prod_records.keys():
                                    raise ProductNotExistError
                                else:
                                    break
                            except (ProductNotExistError):
                                print('The product ID does not exist. Try again...')
                                continue
                        quantity = int(input('Enter quantity: '))
                        if (quantity > prod_records[prod_id].get_stock()):
                            raise QuantityTooLargeError
                        if (prod_records[prod_id].get_price() == None or prod_records[prod_id].get_price() < 0):
                            raise InvalidProductPriceError
                        if (prod_records[prod_id].get_price() == 0):
                            raise FreeProductError
                        # creating order object
                        order = Order(cust_records[cust_id], prod_records[prod_id], quantity)
                        order.set_time(datetime.date.today())
                        
                        # reducing stock by quantity
                        updated_stock = prod_records[prod_id].get_stock() - quantity
                        prod_records[prod_id].set_stock(updated_stock)

                        # get discounted price
                        price = prod_records[prod_id].get_price()
                        total_price = price * quantity

                        # displaying order receipt
                        print(cust_records[cust_id].get_name() + ' purchased ' + str(quantity) + ' x ' + prod_records[prod_id].get_name())
                        print('Unit Price: ' + str(prod_records[prod_id].get_price()))
                        print('Total Price: ' + str(cust_records[cust_id].get_discount(total_price)))
                        print('Purchased Date: ' + str(order.get_time()))
                        print('Remaining Stock: ' + str(prod_records[prod_id].get_stock()))


                    except (QuantityTooLargeError):
                        print('Quantity requested is too large and not enough stock')
                    except InvalidProductPriceError:
                        print('Price for this product is not set yet or is negative')
                    except FreeProductError:
                        print('The product is free')

                # get a product details
                elif value == 4:
                    try:
                        prod_id = input('Enter the product ID: ')
                        if prod_id not in prod_records.keys():
                                raise ProductNotExistError
                        prod_records[prod_id].displayProduct()
                    except ProductNotExistError:
                        print('The product ID does not exist')

                # adjust customer's discount rate
                elif value == 5:
                    try:
                        cust_id = input('Enter customer ID: ')
                        if cust_id not in cust_records.keys():
                            raise InvalidCustomerError
                        new_discount_rate = int(input('Enter new discount rate: '))
                        cust_records[cust_id].setRate(new_discount_rate)
                    except InvalidCustomerError:
                        print('This customer does not exist')
                    except Exception:
                        print('Invalid input')

                # adjust customer's amount threshold
                elif value == 6:
                    try:
                        cust_id = input('Enter customer ID: ')
                        if cust_id not in cust_records.keys():      # also check the customer should be a wholesaler
                            raise InvalidCustomerError
                        new_amount_threshold = int(input('Enter new amount threshold: '))
                        cust_records[cust_id].set_amount_threshold(new_amount_threshold)
                    except InvalidCustomerError:
                        print('This customer does not exist')
                    except Exception:
                        print('Invalid input')

                #display all orders
                elif value == 7:
                    records.listOrders()
                        
                else:
                    print('Incorrect value. Try again')
            except:
                Exception('Exception. Try Again.')


# starting our program
start = Operations()