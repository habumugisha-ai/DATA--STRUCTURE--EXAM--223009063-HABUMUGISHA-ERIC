import tkinter as tk
from tkinter import messagebox

class TreeNode:
    def __init__(self, name, value=None, rate=None):
        self.name = name
        self.value = value  # Meter reading or other values (kWh)
        self.rate = rate    # Rate per kWh
        self.children = []  # Children could be other nodes (like meters)

    def add_child(self, node):
        self.children.append(node)

    def get_node_info(self):
        return f"{self.name}: {self.value}"

    def update_meter_reading(self, new_reading):
        if "Meter" in self.name:
            self.value = new_reading
        else:
            print(f"Cannot update reading for {self.name}, as it's not a meter.")

    def generate_bill(self):
        if "Meter" in self.name and self.rate:
            consumption = self.value
            bill = consumption * self.rate
            return bill
        return 0

class SmartMeteringApp:
    def __init__(self, root, region):
        self.root = root
        self.region = region
        self.create_widgets()

    def create_widgets(self):
        self.root.title("Smart Metering System")

        # Create a label for the title
        self.title_label = tk.Label(self.root, text="Smart Metering System", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Create a frame to hold the hierarchical tree
        self.tree_frame = tk.Frame(self.root)
        self.tree_frame.pack(pady=10)

        # Create a button to generate bills
        self.generate_bill_button = tk.Button(self.root, text="Generate Bill", command=self.generate_bill)
        self.generate_bill_button.pack(pady=10)

        # Create a button to sort meters based on priority (bucket sort)
        self.sort_button = tk.Button(self.root, text="Sort Meters by Priority", command=self.sort_meters)
        self.sort_button.pack(pady=10)

        # Start displaying the tree
        self.display_tree(self.region, self.tree_frame, level=0)

    def display_tree(self, node, parent_frame, level):
        """
        Display the tree node information and its children.
        """
        label = tk.Label(parent_frame, text=node.get_node_info(), font=("Arial", 12))
        label.pack(anchor="w", padx=20 * level)

        # If the node is a meter, apply color coding based on its reading
        if "Meter" in node.name:
            label.config(bg=self.get_meter_status_color(node.value))
        
        # Recursively display children nodes
        for child in node.children:
            self.display_tree(child, parent_frame, level + 1)

    def get_meter_status_color(self, reading):
        """
        Return color based on the reading value.
        Low usage = Green, Normal = Yellow, High = Red
        """
        if reading < 300:
            return "green"
        elif 300 <= reading <= 600:
            return "yellow"
        else:
            return "red"

    def generate_bill(self):
        """
        Generate the bill for the entire region and its sub-hierarchies.
        """
        total_bill = 0
        for substation in self.region.children:
            for segment in substation.children:
                for meter in segment.children:
                    bill = meter.generate_bill()
                    total_bill += bill
                    print(f"Bill for {meter.name}: {bill:.2f} USD")
        
        messagebox.showinfo("Total Bill", f"Total Bill for the Region: {total_bill:.2f} USD")

    def sort_meters(self):
        """
        Sort the meters in the region based on their readings using Bucket Sort.
        """
        all_meters = []

        # Collect all meters in the region
        for substation in self.region.children:
            for segment in substation.children:
                for meter in segment.children:
                    all_meters.append(meter)

        # Perform Bucket Sort
        sorted_meters = self.bucket_sort(all_meters)

        # Clear the tree and re-display the sorted meters
        for widget in self.tree_frame.winfo_children():
            widget.destroy()
        
        self.display_sorted_meters(sorted_meters)

    def bucket_sort(self, meters):
        """
        Sort the meters based on their readings using Bucket Sort.
        """
        # Find the min and max reading to determine bucket range
        min_value = min(meter.value for meter in meters)
        max_value = max(meter.value for meter in meters)
        
        # Number of buckets (let's choose 10 buckets for simplicity)
        num_buckets = 10
        bucket_range = (max_value - min_value) / num_buckets

        # Create empty buckets
        buckets = [[] for _ in range(num_buckets)]

        # Distribute meters into buckets based on their readings
        for meter in meters:
            bucket_index = int((meter.value - min_value) / bucket_range)
            bucket_index = min(bucket_index, num_buckets - 1)  # Ensure it doesn't exceed the last bucket
            buckets[bucket_index].append(meter)

        # Sort each bucket (using insertion sort or another sorting method)
        sorted_meters = []
        for bucket in buckets:
            sorted_meters.extend(sorted(bucket, key=lambda meter: meter.value))

        return sorted_meters

    def display_sorted_meters(self, sorted_meters):
        """
        Display the sorted meters in the Tkinter tree.
        """
        label = tk.Label(self.tree_frame, text="Sorted Meters (By Priority)", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        for meter in sorted_meters:
            meter_label = tk.Label(self.tree_frame, text=meter.get_node_info(), font=("Arial", 12))
            meter_label.pack(anchor="w", padx=20)

# Example Usage:

# Root node representing a region
region = TreeNode("North Region")

# Substation nodes under the region
substation_1 = TreeNode("Substation A")
substation_2 = TreeNode("Substation B")

# Add substations to the region
region.add_child(substation_1)
region.add_child(substation_2)

# Customer segments with rates (e.g., rate in USD per kWh)
residential = TreeNode("Residential", value="Billing Type: Residential", rate=0.12)  # 0.12 USD per kWh
commercial = TreeNode("Commercial", value="Billing Type: Commercial", rate=0.15)  # 0.15 USD per kWh

# Add customer segments to Substation A
substation_1.add_child(residential)
substation_1.add_child(commercial)

# Meters under Residential segment
meter_1 = TreeNode("Meter 101", value=250, rate=residential.rate)  # Reading: 250 kWh
meter_2 = TreeNode("Meter 102", value=300, rate=residential.rate)  # Reading: 300 kWh

# Add meters to Residential segment
residential.add_child(meter_1)
residential.add_child(meter_2)

# Meters under Commercial segment
meter_3 = TreeNode("Meter 201", value=500, rate=commercial.rate)  # Reading: 500 kWh
meter_4 = TreeNode("Meter 202", value=450, rate=commercial.rate)  # Reading: 450 kWh

# Add meters to Commercial segment
commercial.add_child(meter_3)
commercial.add_child(meter_4)

# Customer segment under Substation B
industrial = TreeNode("Industrial", value="Billing Type: Industrial", rate=0.2)  # 0.2 USD per kWh

# Add customer segment to Substation B
substation_2.add_child(industrial)

# Meters under Industrial segment
meter_5 = TreeNode("Meter 301", value=1000, rate=industrial.rate)  # Reading: 1000 kWh

# Add meter to Industrial segment
industrial.add_child(meter_5)

# Set up the Tkinter window
root = tk.Tk()

# Create the SmartMeteringApp
app = SmartMeteringApp(root, region)

# Run the application
root.mainloop()
