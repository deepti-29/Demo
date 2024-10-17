#exception handling
import email


class InvalidDataException(Exception):
    pass

class InsufficientStockException(Exception):
    pass

class PaymentFailedException(Exception):
    pass

class InventoryManager:
    def __init__(self):
        self.ProductsList = []

    def update_customer_info(self, email=None, phone=None):
        if email and "@" not in email:
            raise InvalidDataException("Invalid email format.")

    def AddProduct(self, product):
        if any(p.ProductID == product.ProductID for p in self.ProductsList):
            raise InvalidDataException("Product already exists")
        self.ProductsList.append(product)

    def RemoveProduct(self, product_id):
        product = next((p for p in self.ProductsList if p.ProductID == product_id), None)
        if not product:
            raise InvalidDataException("Product not found")
        self.ProductsList.remove(product)

    def GetProducts(self):
        return [p.GetProductDetails() for p in self.ProductsList]
