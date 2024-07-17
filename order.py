# order.py

from datetime import datetime
from customer import Customer
from order_item import OrderItem

class Order:
    def __init__(self, order_id, name, delivery_address, items, customer: Customer, payment_type, order_type):
        self.id = order_id
        self.name = name
        self.delivery_address = delivery_address
        self.items = items
        self.customer = customer
        self.payment_type = payment_type
        self.order_date = datetime.now()
        self.order_type = order_type
        self.total_price = self.calculate_total_price()
        self.update_customer_favorites()

    def calculate_total_price(self):
        total = sum(item.price for item in self.items)
        if self.order_type == "VIP":
            if self.customer.customer_type != "VIP":
                raise ValueError("Customer is not a VIP customer, but the order is a VIP order.")
            discount = self.customer.discount if self.customer.discount else 0
            total = total * (1 - discount)
        return total

    def update_customer_favorites(self):
        for item in self.items:
            self.customer.add_favorite_item(item)
