# customer.py

from gift import Gift
from order_item import OrderItem

class Customer:
    def __init__(self, cust_id, first_name, last_name, email, delivery_address, customer_type, discount=None):
        self.id = cust_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.delivery_address = delivery_address
        self.customer_type = customer_type
        self.discount = discount
        self.favorite_items = set()
        self.gift = None

    def add_favorite_item(self, item: OrderItem):
        self.favorite_items.add(item.name)

    def remove_favorite_item(self, item_name: str):
        if item_name in self.favorite_items:
            self.favorite_items.remove(item_name)

    def take_gift(self, gift: Gift):
        self.gift = gift

    def open_gift(self):
        if self.gift:
            self.gift.open_gift()
