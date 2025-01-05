class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    # Check if the queue is empty
    def is_empty(self):
        return self.front == -1

    # Check if the queue is full
    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    # Add task to the queue
    def enqueue(self, task):
        if self.is_full():
            print("Queue is full, cannot add more tasks.")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = task
        print(f"Task added: {task}")

    # Remove task from the queue (process the task)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, no task to process.")
            return None
        task = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return task

    # Display the current tasks in the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        i = self.front
        while i != self.rear:
            print(self.queue[i], end=" <- ")
            i = (i + 1) % self.size
        print(self.queue[self.rear])


class SmartMeteringSystem:
    def __init__(self, queue_size):
        self.queue = Queue(queue_size)  # Queue for billing tasks
        self.customers = {}  # Dictionary to store customer details (ID, billing info)

    # Add a customer to the system
    def add_customer(self, customer_id, name):
        self.customers[customer_id] = {"name": name, "total_bill": 0}
        print(f"Customer added: ID = {customer_id}, Name = {name}")

    # Add a task (new meter reading) to the queue for processing
    def add_meter_reading_task(self, customer_id, reading):
        task = {"customer_id": customer_id, "reading": reading}
        self.queue.enqueue(task)

    # Process tasks in the queue (calculate billing)
    def process_tasks(self):
        if self.queue.is_empty():
            print("No tasks to process.")
            return
        task = self.queue.dequeue()
        customer_id = task["customer_id"]
        reading = task["reading"]

        # Assuming the billing is based on the reading (just a simple calculation)
        bill = self.calculate_bill(reading)
        self.customers[customer_id]["total_bill"] += bill

        # Display processed task details
        print(f"Processed task for Customer ID {customer_id}: Reading = {reading}, Bill = {bill}, Total Bill = {self.customers[customer_id]['total_bill']}")

    # Calculate the bill based on meter reading (simple example: 1 unit = 1 unit of currency)
    def calculate_bill(self, reading):
        return reading * 0.1  # Example: 1 unit = 0.1 currency units

    # Display all customers and their billing info
    def display_all_customers(self):
        if not self.customers:
            print("No customers found.")
            return
        print("Customer Billing Information:")
        for customer_id, info in self.customers.items():
            print(f"Customer ID: {customer_id}, Name: {info['name']}, Total Bill: {info['total_bill']}")

    # Display the current tasks in the queue
    def display_queue(self):
        self.queue.display()


# Example Usage of Integrated SmartMeteringSystem with Queue

# Initialize the system with a queue of size 5
system = SmartMeteringSystem(5)

# Adding customers
system.add_customer(101, "Alice")
system.add_customer(102, "Bob")
system.add_customer(103, "Charlie")

# Add meter reading tasks (with readings) to the queue
system.add_meter_reading_task(101, 200)  # Alice's meter reading
system.add_meter_reading_task(102, 150)  # Bob's meter reading
system.add_meter_reading_task(103, 300)  # Charlie's meter reading

# Display current tasks in the queue
system.display_queue()

# Process tasks in the queue (calculating bills based on readings)
system.process_tasks()  # Processes Alice's reading
system.process_tasks()  # Processes Bob's reading
system.process_tasks()  # Processes Charlie's reading

# Display all customer billing info
system.display_all_customers()

# Display tasks in queue after processing
system.display_queue()

# Add another task to the queue and process
system.add_meter_reading_task(101, 220)  # Alice's next meter reading
system.process_tasks()
