class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, task):
        if self.is_full():
            print("Queue is full, cannot add more tasks.")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = task
        print(f"Task added to queue: {task}")

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

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        i = self.front
        while i != self.rear:
            print(self.queue[i], end=" <- ")
            i = (i + 1) % self.size
        print(self.queue[self.rear])


class BSTNode:
    def __init__(self, order_id, customer_id, meter_reading, total_bill):
        self.order_id = order_id
        self.customer_id = customer_id
        self.meter_reading = meter_reading
        self.total_bill = total_bill
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, order_id, customer_id, meter_reading, total_bill):
        new_node = BSTNode(order_id, customer_id, meter_reading, total_bill)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, node, new_node):
        if new_node.order_id < node.order_id:
            if node.left is None:
                node.left = new_node
            else:
                self._insert(node.left, new_node)
        else:
            if node.right is None:
                node.right = new_node
            else:
                self._insert(node.right, new_node)

    def search(self, order_id):
        return self._search(self.root, order_id)

    def _search(self, node, order_id):
        if node is None or node.order_id == order_id:
            return node
        if order_id < node.order_id:
            return self._search(node.left, order_id)
        else:
            return self._search(node.right, order_id)

    def delete(self, order_id):
        self.root = self._delete(self.root, order_id)

    def _delete(self, node, order_id):
        if node is None:
            return node
        if order_id < node.order_id:
            node.left = self._delete(node.left, order_id)
        elif order_id > node.order_id:
            node.right = self._delete(node.right, order_id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_larger_node = self._min_value_node(node.right)
                node.order_id = min_larger_node.order_id
                node.customer_id = min_larger_node.customer_id
                node.meter_reading = min_larger_node.meter_reading
                node.total_bill = min_larger_node.total_bill
                node.right = self._delete(node.right, min_larger_node.order_id)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        result = []
        if node is not None:
            result.extend(self._inorder(node.left))
            result.append({
                'order_id': node.order_id,
                'customer_id': node.customer_id,
                'meter_reading': node.meter_reading,
                'total_bill': node.total_bill
            })
            result.extend(self._inorder(node.right))
        return result


class SmartMeteringSystem:
    def __init__(self, queue_size):
        self.queue = Queue(queue_size)
        self.orders_tree = BST()  # Binary Search Tree to manage orders

    def add_customer_order(self, order_id, customer_id, meter_reading, total_bill):
        self.orders_tree.insert(order_id, customer_id, meter_reading, total_bill)
        print(f"Order added: Order ID = {order_id}, Customer ID = {customer_id}, Meter Reading = {meter_reading}, Total Bill = {total_bill}")

    def add_meter_reading_task(self, customer_id, reading):
        task = {"customer_id": customer_id, "reading": reading}
        self.queue.enqueue(task)

    def process_tasks(self):
        if self.queue.is_empty():
            print("No tasks to process.")
            return
        task = self.queue.dequeue()
        customer_id = task["customer_id"]
        reading = task["reading"]

        # Calculate the bill (example logic: 1 unit = 0.1 currency unit)
        bill = reading * 0.1
        order_id = customer_id * 1000  # Generate an order ID based on customer_id
        self.add_customer_order(order_id, customer_id, reading, bill)

    def display_all_orders(self):
        orders = self.orders_tree.inorder()
        if not orders:
            print("No orders to display.")
        else:
            print("Orders in Sorted Order (by Order ID):")
            for order in orders:
                print(order)

    def display_queue(self):
        self.queue.display()


# Example Usage of Integrated SmartMeteringSystem with Queue and BST

# Initialize the system with a queue of size 5
system = SmartMeteringSystem(5)

# Add meter reading tasks to the queue
system.add_meter_reading_task(101, 200)  # Customer 101 with a reading of 200
system.add_meter_reading_task(102, 150)  # Customer 102 with a reading of 150
system.add_meter_reading_task(103, 300)  # Customer 103 with a reading of 300

# Display current tasks in the queue
system.display_queue()

# Process tasks in the queue (calculates bill and adds to BST)
system.process_tasks()  # Process task for Customer 101
system.process_tasks()  # Process task for Customer 102
system.process_tasks()  # Process task for Customer 103

# Display all customer orders stored in the BST
system.display_all_orders()

# Add another task to the queue and process it
system.add_meter_reading_task(104, 220)  # Customer 104 with a reading of 220
system.process_tasks()

# Display orders after processing the new task
system.display_all_orders()

# Display current tasks in the queue after processing
system.display_queue()
