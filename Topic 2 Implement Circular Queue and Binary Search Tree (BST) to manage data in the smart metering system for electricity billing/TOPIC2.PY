class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, reading):
        if self.is_full():
            self.front = (self.front + 1) % self.size
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = reading

    def dequeue(self):
        if self.is_empty():
            return None
        removed_reading = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return removed_reading

    def display(self):
        if self.is_empty():
            return
        index = self.front
        while index != self.rear:
            print(self.queue[index], end=" -> ")
            index = (index + 1) % self.size
        print(self.queue[self.rear])


class Node:
    def __init__(self, customer_id, name, billing_info):
        self.customer_id = customer_id
        self.name = name
        self.billing_info = billing_info
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, customer_id, name, billing_info):
        self.root = self._insert(self.root, customer_id, name, billing_info)

    def _insert(self, node, customer_id, name, billing_info):
        if node is None:
            return Node(customer_id, name, billing_info)
        if customer_id < node.customer_id:
            node.left = self._insert(node.left, customer_id, name, billing_info)
        else:
            node.right = self._insert(node.right, customer_id, name, billing_info)
        return node

    def search(self, customer_id):
        return self._search(self.root, customer_id)

    def _search(self, node, customer_id):
        if node is None or node.customer_id == customer_id:
            return node
        if customer_id < node.customer_id:
            return self._search(node.left, customer_id)
        else:
            return self._search(node.right, customer_id)

    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(f"Customer ID: {node.customer_id}, Name: {node.name}, Billing Info: {node.billing_info}")
            self._inorder(node.right)


circular_queue = CircularQueue(5)
circular_queue.enqueue(100)
circular_queue.enqueue(150)
circular_queue.enqueue(200)
circular_queue.enqueue(250)
circular_queue.enqueue(300)
circular_queue.enqueue(350)
circular_queue.display()
circular_queue.dequeue()
circular_queue.display()

bst = BST()
bst.insert(101, "John Doe", "Last Bill: $200")
bst.insert(102, "Jane Smith", "Last Bill: $150")
bst.insert(103, "Alice Johnson", "Last Bill: $120")
bst.inorder()

customer = bst.search(102)
if customer:
    print(f"Found customer: {customer.name} with {customer.billing_info}")
else:
    print("Customer not found.")
