user = {
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

print(f"\nUser Information:\n User at ID {user['id']} is {user['name']}, aged {user['age']} from {user['city']}.")

user["role"] = "Developer"

print(f"user after adding role: {user}")

order = {
    "order_id": 101,
    "product": "Laptop",
    "quantity": 2,
    "price": 1200.50
}


print(f"\nOrder Information:\n Order ID {order['order_id']} for {order['product']} (Quantity: {order['quantity']}) at ${order['price']:.2f} each.\n")

class DeliveryTask:
    def __init__(self, task_id, vendor_name, delivery_date):
        self.task_id = task_id
        self.vendor_name = vendor_name
        self.delivery_date = delivery_date
        self.status = "Pending"
    def __str__(self):
        return f"Delivery Task {self.task_id} for {self.vendor_name} scheduled on {self.delivery_date} is currently {self.status}."
    def __repr__(self):
        return f"DeliveryTask(task_id={self.task_id}, vendor_name='{self.vendor_name}', delivery_date='{self.delivery_date}', status='{self.status}')"

    def update_delivery_date(self, new_date):
        self.delivery_date = new_date
        print(f"Delivery Task {self.task_id} for {self.vendor_name} has been rescheduled to {self.delivery_date}.")

    def update_status(self, new_status):
        self.status = new_status
        print(f"Delivery Task {self.task_id} for {self.vendor_name} is now marked as {self.status}.")

    def mark_completed(self):
        self.status = "Completed"
        print(f"Delivery Task {self.task_id} for {self.vendor_name} scheduled on {self.delivery_date} has been marked as completed.")

task1 = DeliveryTask(201, "Vendor A", "2024-06-15")
print(f"\n{task1}")


task1.update_delivery_date("2024-06-20")
task1.update_status("In Progress")
task1.mark_completed()