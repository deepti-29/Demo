#composition
class Orders:
    def __init__(self, order_id, customer, order_date, total_amount):
        self.__OrderID = order_id
        self.__Customer = customer  
        self.__OrderDate = order_date
        self.__TotalAmount = total_amount

    @property
    def Customer(self):
        return self.__Customer

    def GetOrderDetails(self):
        return f"OrderID: {self.__OrderID}, Customer: {self.__Customer.GetCustomerDetails()}, Order Date: {self.__OrderDate}"

class OrderDetails:
    def __init__(self, order_detail_id, order, product, quantity):
        self.__OrderDetailID = order_detail_id
        self.__Order = order  
        self.__Product = product  
        self.__Quantity = quantity

    @property
    def Order(self):
        return self.__Order

    @property
    def Product(self):
        return self.__Product
