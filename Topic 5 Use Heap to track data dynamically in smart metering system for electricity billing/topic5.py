class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(self.heap) and self.heap[left]['total_bill'] < self.heap[smallest]['total_bill']:
            smallest = left
        if right < len(self.heap) and self.heap[right]['total_bill'] < self.heap[smallest]['total_bill']:
            smallest = right
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify(smallest)

    def insert(self, order_id, customer_id, meter_reading, total_bill):
        self.heap.append({'order_id': order_id, 'customer_id': customer_id, 'meter_reading': meter_reading, 'total_bill': total_bill})
        index = len(self.heap) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index]['total_bill'] < self.heap[parent]['total_bill']:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def remove_min(self):
        if len(self.heap) == 0:
            return None
        min_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return min_item

    def get_min(self):
        return self.heap[0] if self.heap else None

    def display(self):
        if not self.heap:
            print("Heap is empty.")
        else:
            for item in self.heap:
                print(item)


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, customer_order):
        self.queue.append(customer_order)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None

    def display(self):
        if not self.queue:
            print("Queue is empty.")
        else:
            for customer in self.queue:
                print(customer)


class BSTNode:
    def __init__(self, order_id, customer_id, total_bill):
        self.order_id = order_id
        self.customer_id = customer_id
        self.total_bill = total_bill
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, order_id, customer_id, total_bill):
        if self.root is None:
            self.root = BSTNode(order_id, customer_id, total_bill)
        else:
            self._insert(self.root, order_id, customer_id, total_bill)

    def _insert(self, node, order_id, customer_id, total_bill):
        if order_id < node.order_id:
            if node.left is None:
                node.left = BSTNode(order_id, customer_id, total_bill)
            else:
                self._insert(node.left, order_id, customer_id, total_bill)
        else:
            if node.right is None:
                node.right = BSTNode(order_id, customer_id, total_bill)
            else:
                self._insert(node.right, order_id, customer_id, total_bill)

    def search(self, order_id):
        return self._search(self.root, order_id)

    def _search(self, node, order_id):
        if node is None or node.order_id == order_id:
            return node
        if order_id < node.order_id:
            return self._search(node.left, order_id)
        return self._search(node.right, order_id)

    def display_in_order(self):
        self._in_order(self.root)

    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(f"Order ID: {node.order_id}, Customer ID: {node.customer_id}, Total Bill: {node.total_bill}")
            self._in_order(node.right)


class SmartMeteringSystem:
    def __init__(self):
        self.min_heap = MinHeap()
        self.queue = Queue()
        self.bst = BST()

    def add_customer_order(self, order_id, customer_id, meter_reading, total_bill):
        self.min_heap.insert(order_id, customer_id, meter_reading, total_bill)
        self.bst.insert(order_id, customer_id, total_bill)
        print(f"Order added: Order ID = {order_id}, Customer ID = {customer_id}, Meter Reading = {meter_reading}, Total Bill = {total_bill}")

    def process_meter_reading(self, customer_id, reading):
        total_bill = reading * 0.1
        order_id = customer_id * 1000
        self.queue.enqueue({'order_id': order_id, 'customer_id': customer_id, 'meter_reading': reading, 'total_bill': total_bill})
        print(f"Reading processed: Customer ID = {customer_id}, Meter Reading = {reading}, Total Bill = {total_bill}")

    def process_and_remove_min_bill(self):
        min_order = self.min_heap.remove_min()
        if min_order:
            print(f"Processed order with minimum bill: {min_order}")
        else:
            print("No orders to process.")

    def display_all_orders_in_queue(self):
        print("Queue Orders:")
        self.queue.display()

    def display_all_orders_in_bst(self):
        print("BST Orders (Sorted by Order ID):")
        self.bst.display_in_order()

    def display_all_orders_in_heap(self):
        print("Heap Orders (Sorted by Bill):")
        self.min_heap.display()


system = SmartMeteringSystem()

system.process_meter_reading(101, 200)
system.process_meter_reading(102, 150)
system.process_meter_reading(103, 300)

system.add_customer_order(101000, 101, 200, 20.0)
system.add_customer_order(102000, 102, 150, 15.0)
system.add_customer_order(103000, 103, 300, 30.0)

system.display_all_orders_in_queue()
system.display_all_orders_in_heap()
system.display_all_orders_in_bst()

system.process_and_remove_min_bill()

system.display_all_orders_in_heap()
