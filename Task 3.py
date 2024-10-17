# Customer Class with Encapsulation
class Customer:
    def _init_(self, customer_id, first_name, last_name, email, phone, address):
        self._customer_id = customer_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._address = address
        self._orders = []  

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._first_name = name
        else:
            raise ValueError("First name must be a non-empty string")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._last_name = name
        else:
            raise ValueError("Last name must be a non-empty string")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
        else:
            raise ValueError("Invalid email address")

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, new_phone):
        if new_phone.isdigit() and len(new_phone) == 10:
            self._phone = new_phone
        else:
            raise ValueError("Phone number must be a 10-digit number")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, new_address):
        if isinstance(new_address, str) and len(new_address) > 0:
            self._address = new_address
        else:
            raise ValueError("Address must be a non-empty string")

    def calculate_total_orders(self):
        return len(self._orders)

    def get_customer_details(self):
        return {
            "CustomerID": self._customer_id,
            "FirstName": self._first_name,
            "LastName": self._last_name,
            "Email": self._email,
            "Phone": self._phone,
            "Address": self._address
        }

    def update_customer_info(self, email=None, phone=None, address=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address
        return "Customer info updated successfully"


# Product Class with Encapsulation
class Product:
    def _init_(self, product_id, product_name, description, price):
        self._product_id = product_id
        self._product_name = product_name
        self._description = description
        self._price = price

    # Getters and Setters with Validation
    @property
    def product_id(self):
        return self._product_id

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._product_name = name
        else:
            raise ValueError("Product name must be a non-empty string")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, desc):
        if isinstance(desc, str):
            self._description = desc
        else:
            raise ValueError("Description must be a string")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative")

    def get_product_details(self):
        return {
            "ProductID": self._product_id,
            "ProductName": self._product_name,
            "Description": self._description,
            "Price": self._price
        }

    def update_product_info(self, price=None, description=None):
        if price is not None:
            self.price = price  # Validation handled in setter
        if description is not None:
            self.description = description
        return "Product info updated successfully"


# Order Class with Encapsulation
class Order:
    def _init_(self, order_id, customer, order_date, total_amount):
        self._order_id = order_id
        self._customer = customer  # Composition
        self._order_date = order_date
        self._total_amount = total_amount
        self._status = "Pending"
        self._order_details = []

    @property
    def order_id(self):
        return self._order_id

    @property
    def customer(self):
        return self._customer

    @property
    def order_date(self):
        return self._order_date

    @order_date.setter
    def order_date(self, new_date):
        if isinstance(new_date, str):
            self._order_date = new_date
        else:
            raise ValueError("Invalid order date format")

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        if value >= 0:
            self._total_amount = value
        else:
            raise ValueError("Total amount cannot be negative")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        if new_status in ["Pending", "Shipped", "Cancelled"]:
            self._status = new_status
        else:
            raise ValueError("Invalid status")

    def calculate_total_amount(self):
        self._total_amount = sum([detail.calculate_subtotal() for detail in self._order_details])
        return self._total_amount

    def get_order_details(self):
        return {
            "OrderID": self._order_id,
            "Customer": self._customer.get_customer_details(),
            "OrderDate": self._order_date,
            "TotalAmount": self._total_amount,
            "Status": self._status,
            "OrderDetails": [detail.get_order_detail_info() for detail in self._order_details]
        }

    def update_order_status(self, new_status):
        self.status = new_status  # Validation handled in setter
        return f"Order status updated to {new_status}"

    def cancel_order(self):
        self.status = "Cancelled"
        return "Order cancelled successfully"


# OrderDetail Class with Encapsulation
class OrderDetail:
    def _init_(self, order_detail_id, order, product, quantity):
        self._order_detail_id = order_detail_id
        self._order = order  # Composition
        self._product = product  # Composition
        self._quantity = quantity

    @property
    def order_detail_id(self):
        return self._order_detail_id

    @property
    def order(self):
        return self._order

    @property
    def product(self):
        return self._product

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance(value, int) and value > 0:
            self._quantity = value
        else:
            raise ValueError("Quantity must be a positive integer")

    def calculate_subtotal(self):
        return self._product.price * self._quantity

    def get_order_detail_info(self):
        return {
            "OrderDetailID": self._order_detail_id,
            "OrderID": self._order.order_id,
            "Product": self._product.get_product_details(),
            "Quantity": self._quantity,
            "Subtotal": self.calculate_subtotal()
        }

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity  # Validation handled in setter
        return "Quantity updated successfully"


# Inventory Class with Encapsulation
class Inventory:
    def _init_(self, inventory_id, product, quantity_in_stock, last_stock_update):
        self._inventory_id = inventory_id
        self._product = product  # Composition
        self._quantity_in_stock = quantity_in_stock
        self._last_stock_update = last_stock_update

    @property
    def inventory_id(self):
        return self._inventory_id

    @property
    def product(self):
        return self._product

    @property
    def quantity_in_stock(self):
        return self._quantity_in_stock

    @quantity_in_stock.setter
    def quantity_in_stock(self, quantity):
        if isinstance(quantity, int) and quantity >= 0:
            self._quantity_in_stock = quantity
        else:
            raise ValueError("Quantity in stock must be a non-negative integer")

    def get_product(self):
        return self._product

    def get_quantity_in_stock(self):
        return self._quantity_in_stock

    def add_to_inventory(self, quantity):
        if isinstance(quantity, int) and quantity > 0:
            self._quantity_in_stock += quantity
            return "Inventory updated"
        else:
            raise ValueError("Quantity to add must be a positive integer")

    def remove_from_inventory(self, quantity):
        if isinstance(quantity, int) and self._quantity_in_stock >= quantity:
            self._quantity_in_stock -= quantity
            return "Inventory reduced"
        else:
            return "Not enough stock or invalid quantity"

    def update_stock_quantity(self, new_quantity):
        self.quantity_in_stock = new_quantity  # Validation handled in setter
        return "Stock quantity updated"

    def is_product_available(self, quantity_to_check):
        return self._quantity_in_stock >= quantity_to_check

    def get_inventory_value(self):
        return self._product.price * self._quantity_in_stock

    def list_low_stock_products(self, threshold):
        if self._quantity_in_stock < threshold:
            return self._product.get_product_details()
        return None

    def list_out_of_stock_products(self):
        if self._quantity_in_stock == 0:
            return self._product.get_product_details()
        return None

    def list_all_products(self):
        return self._product.get_product_details(), self._quantity_in_stock