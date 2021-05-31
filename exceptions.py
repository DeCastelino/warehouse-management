
class QuantityTooLargeError (Exception):
    """Raised when the requested quantity is too large"""
    pass

class ProductNotExistError (Exception):
    """Raised when the input product ID or name does not exist"""
    pass

class InvalidProductPriceError (Exception):
    """Raised when product price is not set or negative and user tries to order it"""
    pass

class FreeProductError (Exception):
    """Raised when customer trying to order free product"""

class NewCustomerException (Exception):
    """Raised when new customer needs to be created"""

class InvalidCustomerError (Exception):
    """Raised when customer does not exist"""