from datetime import datetime


class OrderItem:
    def __init__(self, item_id, name, price):
        self.id = item_id
        self.name = name
        self.price = price


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

    def take_gift(self, gift1):
        self.gift = gift1

    def open_gift(self):
        if self.gift:
            self.gift.open_gift()


class Gift:
    @staticmethod
    def open_gift():
        print("Congratulations! you got a new gift! Enjoy!")


class Order:
    def __init__(self, order_id, name, delivery_address, items, customer, payment_type, order_type):
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


# Example Usage:
# Creating OrderItems
item1 = OrderItem(1, "Pizza", 10.0)
item2 = OrderItem(2, "Pasta", 8.0)
item3 = OrderItem(3, "Salad", 5.0)
item4 = OrderItem(4, "Soda", 2.5)

# Creating a VIP Customer
vip_customer = Customer(1, "John", "Doe", "john.doe@example.com", "123 VIP St", "VIP", 0.1)

# Creating a Regular Customer
regular_customer = Customer(2, "Jane", "Smith", "jane.smith@example.com", "456 Regular Ave", "REGULAR")

# Creating Orders
vip_order = Order(1, "VIP Order", "123 VIP St", [item1, item2], vip_customer, "CREDIT CARD", "VIP")
regular_order = Order(2, "Regular Order", "456 Regular Ave", [item1], regular_customer, "CASH", "REGULAR")

print("VIP Order Total Price:", vip_order.total_price)
print("Regular Order Total Price:", regular_order.total_price)

# Creating another VIP Customer
vip_customer2 = Customer(3, "Alice", "Brown", "alice.brown@example.com", "789 VIP Road", "VIP", 0.15)

# Creating another Regular Customer
regular_customer2 = Customer(4, "Bob", "Johnson", "bob.johnson@example.com", "321 Regular Lane", "REGULAR")

# Creating Orders for VIP Customer
vip_order2 = Order(3, "VIP Order 2", "789 VIP Road", [item1, item3, item4], vip_customer2, "CHECK", "VIP")

# Creating Orders for Regular Customer
regular_order2 = Order(4, "Regular Order 2", "321 Regular Lane", [item2, item3], regular_customer2, "CREDIT CARD",
                       "REGULAR")

# Printing Order Total Prices
print("VIP Order 2 Total Price:", vip_order2.total_price)
print("Regular Order 2 Total Price:", regular_order2.total_price)

# Checking and printing favorite items
print("VIP Customer 2 Favorite Items:", vip_customer2.favorite_items)
print("Regular Customer 2 Favorite Items:", regular_customer2.favorite_items)

# Adding and opening a gift for Regular customer
gift = Gift()
regular_customer2.take_gift(gift)
regular_customer2.open_gift()

# Adding an item to favorite items directly
regular_customer2.add_favorite_item(item1)
print("Regular Customer 2 Favorite Items after adding Pizza:", regular_customer2.favorite_items)

# Removing an item from favorite items
regular_customer2.remove_favorite_item("Pizza")
print("Regular Customer 2 Favorite Items after removing Pizza:", regular_customer2.favorite_items)
