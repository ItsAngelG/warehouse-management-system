# warehouse-management-system
Python warehouse management system using data structures for inventory, order processing, and warehouse connectivity
Python Version: Python 3.13.2

## Functions

### Inventory

lookup_inventory()
This function searches the inventory for a product and returns the amount currently in stock.

update_inventory()
This function updates the inventory amount for existing products.
Negative values and non existent products raises error.

add_product()
This function adds a new product to the inventory. It raises an error if the product already exists or if a negative quantity is provided.

remove_product()
This function removes a product from the inventory. It raises an error if the product does not exist.

get_inventory_info()
This function shows the current inventory information. It raises an error if the inventory is empty.

### Order Queue

add_order()
This function adds a new order to the order queue.
It raises error if empty order is provided.

process_order()
This function is used to process next order using first in, first, out.
It raises error if there are no orders to process.

get_order_status()
This function provides the current status of an order. It raises error if the order does not exist.

### Warehouses

connect_warehouses()
This function connects two existing warehouses for shipping.
It raises error if one or both warehouses do not exist.

track_warehouse_space()
This function provide the available space for a warehouse. It raises an error if the warehouse does not exist.

update_warehouse_space()
This function updates the available warehouse space when items are added or removed. It raises error if the warehouse does not exist or if the avaliable space would become negative.

add_warehouse()
This function adds a new warehouse to the system. It raises an error if the warehouse already exists or if negative space is provided.

## Running the functions

1. Open project in VS Code
2. Install Python
3. Open terminal
4. Run Python file _main.py_

## Error Handling & Edge Case

The functions include error handling for invalid inputs and edge cases. The inventory functions handle missing
products, duplicate products, empty inventory, and negative quantities. The order function handle empty
orders, empty queues, and orders that cannot be found. The warehouse function handles non existent
warehouses, duplicate warehouses, negative warehouse space, and invalid warehouse connections.
