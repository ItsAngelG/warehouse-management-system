#INVENTORY

inventory = {
    "laptop": 50,
    "keyboard": 100,
    "mouse": 200
}

# Inventory lookup system that searches for products 
# If product is not found, message product not found in inventory 
# If product is found, the total amount in stock will print

def lookup_inventory(inventory, product):
    if product not in inventory: 
        raise ValueError("Product not found in inventory")
    return inventory[product]


#testing lookup_inventory()

print(lookup_inventory(inventory, "laptop"))

try:
    lookup_inventory(inventory, "phone")
except ValueError as error:
    print("Error test:", error)



# Inventory updates only if the product is in 
# the inventory and isn't less than 0

def update_inventory(inventory, product, quantity):
    if product not in inventory:
        raise ValueError("Product not found in inventory")
    
    if quantity < 0:
        raise ValueError("No negative product value")

    inventory[product] = quantity


#testing update_inventory()

update_inventory(inventory, "mouse", 230)
print(inventory)

try:
    update_inventory(inventory, "mouse", -10)
except ValueError as error:
    print("Error test:", error)



def add_product(inventory, product, quantity):
    if product in inventory:
        raise ValueError("Product already exist in inventory")
    if quantity < 0:
        raise ValueError("No negative product value")

    inventory[product] = quantity


#testing add_product

add_product(inventory, "monitor", 5)
print(inventory)

try:
    add_product(inventory, "laptop", 5)
except ValueError as error:
    print("Error test:", error)



def remove_product(inventory, product):
    if product not in inventory:
        raise ValueError("Product is not in inventory")

    del inventory[product]


#testing remove_product()

remove_product(inventory, "laptop")
print(inventory)

try:
    remove_product(inventory, "cable")
except ValueError as error:
    print("Error test:", error)



def get_inventory_info(inventory):
    if not inventory:
        raise ValueError("Inventory is empty")
    return inventory


#Testing get_inventory_info

print("Inventory Information:", get_inventory_info(inventory))

try:
    get_inventory_info({})
except ValueError as error:
    print("Error test:", error)





#ORDER QUEUE

#Using Python Library
from collections import deque

orders = deque()
order_status = {}



def add_order(order_queue, order):
    if not order:
        raise ValueError("Order cannot be empty")

    order_queue.append(order)
    order_status[order] = "Pending"


def process_order(order_queue):
    if not order_queue:
        raise ValueError("There are no orders to process")

    order = order_queue.popleft()
    order_status[order] = "Processed"
    return order


#Testing the function
add_order(orders, "Order 001")
add_order(orders, "Order 002")
add_order(orders, "Order 003")

print(orders)

print("processed:", process_order(orders))
print("processed:", process_order(orders))
print("processed:", process_order(orders))

print("remaining orders:", orders)

try:
    add_order(orders, "")
except ValueError as error:
    print("Error test:", error)

try:
    process_order(orders)
except ValueError as error:
    print("Error test:", error)



def get_order_status(order_status, order):
    if order not in order_status:
        raise ValueError("Order not found")
    return order_status[order]

#Testing get_order_status
print("Order 001 status:", get_order_status(order_status, "Order 001"))

try:
    get_order_status(order_status, "Order 900")
except ValueError as error:
    print("Error test:", error)





#WAREHOUSES

warehouses = {
    "Texas": {"space": 1000, "connections": []},
    "California": {"space": 1500, "connections": []},
    "Oklahoma": {"space": 2000, "connections": []},
}

#Connects two existing warehouses for shipping
def connect_warehouses(warehouses, warehouse1, warehouse2):
    if warehouse1 not in warehouses or warehouse2 not in warehouses:
        raise ValueError("Warehouse does not exist")

    warehouses[warehouse1]["connections"].append(warehouse2)
    warehouses[warehouse2]["connections"].append(warehouse1)

#Testing Warehouse Function 
connect_warehouses(warehouses, "Texas", "California")
print(warehouses)

try:
    connect_warehouses(warehouses, "Texas", "Florida")
except ValueError as error:
    print("Error test:", error)



def track_warehouse_space(warehouses, warehouse):
    if warehouse not in warehouses:
        raise ValueError("Warehouse does not exist")

    return warehouses[warehouse]["space"]


#Testing track_warehouse_space()
print("Texas avaliable space:", track_warehouse_space(warehouses, "Texas"))

try:
    track_warehouse_space(warehouses, "New York")
except ValueError as error:
    print("Error test:", error)



def update_warehouse_space(inventory, warehouse, space_change):
    if warehouse not in warehouses:
        raise ValueError("Warehouse does not exist")

    if warehouses[warehouse]["space"] + space_change < 0:
        raise ValueError("Warehouse space cannot be negative")

    warehouses[warehouse]["space"] += space_change

#Testing update_warehouse_space()
update_warehouse_space(warehouses, "Texas", -100)
print("Texas avaliable space:", track_warehouse_space(warehouses, "Texas"))

update_warehouse_space(warehouses, "Texas", 50)
print("Texas avaliable space:", track_warehouse_space(warehouses, "Texas"))

try:
    update_warehouse_space(warehouses, "Florida", -100)
except ValueError as error:
    print("Error Test:", error)

try:
    update_warehouse_space(warehouses, "Texas", -2000)
except ValueError as error:
    print("Error Test:", error)



def add_warehouse(warehouses, warehouse, space):
    if warehouse in warehouses:
        raise ValueError("Warehouse already exist")

    if space < 0:
        raise ValueError("Warehouse space cannot be a negative")

    warehouses[warehouse] = {
        "space": space,
        "connections": []
    }


#Testing add_warehouse()

add_warehouse(warehouses, "New York", 1800)
print(warehouses)

try:
    add_warehouse(warehouses, "Texas", 1800)
except ValueError as error:
    print("Error test:", error)

try:
    add_warehouse(warehouses, "Florida", -1800)
except ValueError as error:
        print("Error test:", error)