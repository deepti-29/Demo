from datetime import datetime
# Customers Class
class Customer:
    def _init_(self, customer_id, first_name, last_name, email, phone, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.orders = []

    def calculate_total_orders(self):
        return len(self.orders)

    def get_customer_details(self):
        return {
            "CustomerID": self.customer_id,
            "FirstName": self.first_name,
            "LastName": self.last_name,
            "Email": self.email,
            "Phone": self.phone,
            "Address": self.address
        }

    def update_customer_info(self, email=None, phone=None, address=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address
        return "Customer info updated successfully"

# Products Class
class Product:
    def _init_(self, product_id, product_name, description, price):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.in_stock = True

    def get_product_details(self):
        return {
            "ProductID": self.product_id,
            "ProductName": self.product_name,
            "Description": self.description,
            "Price": self.price
        }

    def update_product_info(self, price=None, description=None):
        if price:
            self.price = price
        if description:
            self.description = description
        return "Product info updated successfully"

    def is_product_in_stock(self):
        return self.in_stock

# Orders Class
class Order:
    def _init_(self, order_id, customer, order_date, total_amount):
        self.order_id = order_id
        self.customer = customer
        self.order_date = order_date
        self.total_amount = total_amount
        self.status = "Pending"
        self.order_details = []

    def calculate_total_amount(self):
        self.total_amount = sum([detail.calculate_subtotal() for detail in self.order_details])
        return self.total_amount

    def get_order_details(self):
        details = {
            "OrderID": self.order_id,
            "Customer": self.customer.get_customer_details(),
            "OrderDate": self.order_date,
            "TotalAmount": self.total_amount,
            "Status": self.status,
            "OrderDetails": [detail.get_order_detail_info() for detail in self.order_details]
        }
        return details

    def update_order_status(self, new_status):
        self.status = new_status
        return f"Order status updated to {new_status}"

    def cancel_order(self):
        self.status = "Cancelled"
        for detail in self.order_details:
            detail.product.in_stock = True
        return "Order cancelled successfully"

# OrderDetails Class
class OrderDetail:
    def _init_(self, order_detail_id, order, product, quantity):
        self.order_detail_id = order_detail_id
        self.order = order
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self):
        return self.product.price * self.quantity

    def get_order_detail_info(self):
        return {
            "OrderDetailID": self.order_detail_id,
            "OrderID": self.order.order_id,
            "Product": self.product.get_product_details(),
            "Quantity": self.quantity,
            "Subtotal": self.calculate_subtotal()
        }

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        return "Quantity updated successfully"

    def add_discount(self, discount_percentage):
        discounted_price = self.product.price * (1 - discount_percentage / 100)
        return discounted_price * self.quantity

# Inventory Class
class Inventory:
    def _init_(self, inventory_id, product, quantity_in_stock, last_stock_update):
        self.inventory_id = inventory_id
        self.product = product
        self.quantity_in_stock = quantity_in_stock
        self.last_stock_update = last_stock_update

    def get_product(self):
        return self.product

    def get_quantity_in_stock(self):
        return self.quantity_in_stock

    def add_to_inventory(self, quantity):
        self.quantity_in_stock += quantity
        self.last_stock_update = datetime.now()
        return "Inventory updated"

    def remove_from_inventory(self, quantity):
        if self.quantity_in_stock >= quantity:
            self.quantity_in_stock -= quantity
            self.last_stock_update = datetime.now()
            return "Inventory reduced"
        else:
            return "Not enough stock"

    def update_stock_quantity(self, new_quantity):
        self.quantity_in_stock = new_quantity
        self.last_stock_update = datetime.now()
        return "Stock quantity updated"

    def is_product_available(self, quantity_to_check):
        return self.quantity_in_stock >= quantity_to_check

    def get_inventory_value(self):
        return self.product.price * self.quantity_in_stock

    def list_low_stock_products(self, threshold):
        if self.quantity_in_stock < threshold:
            return self.product.get_product_details()
        else:
            return None

    def list_out_of_stock_products(self):
        if self.quantity_in_stock == 0:
            return self.product.get_product_details()
        else:
            return None

    def list_all_products(self):
        return self.product.get_product_details(), self.quantity_in_stock