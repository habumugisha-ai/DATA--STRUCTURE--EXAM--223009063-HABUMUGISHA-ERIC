class TreeNode:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        indent = " " * (level * 4)
        print(f"{indent}{self.name}: {self.value}")
        for child in self.children:
            child.display(level + 1)

class SmartMeteringTree:
    def __init__(self):
        self.root = None

    def set_root(self, root_node):
        self.root = root_node

    def display_tree(self):
        if self.root:
            self.root.display()
        else:
            print("Tree is empty")

root_node = TreeNode("Smart Metering System")

north_region = TreeNode("North Region")
south_region = TreeNode("South Region")

root_node.add_child(north_region)
root_node.add_child(south_region)

north_customer1 = TreeNode("Customer 101", value="Meter Reading: 200, Bill: $20")
north_customer2 = TreeNode("Customer 102", value="Meter Reading: 150, Bill: $15")
south_customer1 = TreeNode("Customer 201", value="Meter Reading: 300, Bill: $30")

north_region.add_child(north_customer1)
north_region.add_child(north_customer2)
south_region.add_child(south_customer1)

north_customer1_meter1 = TreeNode("Meter 1", value="Reading: 200, Bill: $20")
north_customer2_meter1 = TreeNode("Meter 1", value="Reading: 150, Bill: $15")
south_customer1_meter1 = TreeNode("Meter 1", value="Reading: 300, Bill: $30")

north_customer1.add_child(north_customer1_meter1)
north_customer2.add_child(north_customer2_meter1)
south_customer1.add_child(south_customer1_meter1)

tree = SmartMeteringTree()
tree.set_root(root_node)

tree.display_tree()
