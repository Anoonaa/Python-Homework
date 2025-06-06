# homework_inventory_mod.py
# Purpose: Module for inventory system functions, with homework tasks to complete.
# Instructions: Fill in the TODO sections for Tasks 2 and 3.
# This file includes existing functions and partial code for new features.

# Import json for saving inventory to a file
import json

# Display menu with current options
# Note: Menu only shows options 1-8; you'll update inventory.py for option 10
def display_menu():
    print("\nInventory System Menu:")
    print("1. View all items")
    print("2. Add an item")
    print("3. Delete an item")
    print("4. Quit")
    print("5. Search for an item")
    print("6. Update item quantity")
    print("7. Clear inventory")
    print("8. Find low stock items")

# View inventory: Shows all items in the dictionary
def view_inventory(inventory):
    # Check if inventory is empty
    if not inventory:
        print("No items in inventory.")
    else:
        # Print each item with a number
        print("\nInventory:")
        for i, (name, quantity) in enumerate(inventory.items(), 1):
            print(f"{i}. {name} (Quantity: {quantity})")

# Add item: Adds a new item to the inventory
# Task 2: You'll add name validation here
def add_item(inventory, name, quantity):
    try:
        # Check if name is empty
        if not name.strip():
            raise ValueError("Item name cannot be empty.")
        # TODO (Task 2): Validate that name contains only letters and spaces
        # Hint: Use name.replace(" ", "").isalpha() to check
        # Raise ValueError("Item name must contain only letters and spaces.") if invalid
        # Example: "Apple Pie" is valid, "Apple123" is not
        # --- Your code here ---
        
        # Check quantity is valid
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        # Check if item already exists (case-insensitive)
        if name.lower() in (key.lower() for key in inventory):
            print(f"Item {name} already exists!")
            return False
        # Add item to dictionary
        inventory[name] = quantity
        print(f"Added {name} with quantity {quantity}.")
        return True
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return False

# Delete item: Removes an item from the inventory
def delete_item(inventory, name):
    try:
        # Loop through keys (use list to avoid runtime error)
        for key in list(inventory.keys()):
            # Case-insensitive match
            if key.lower() == name.lower():
                del inventory[key]
                print(f"Deleted {name}.")
                return True
        print(f"Item {name} not found.")
        return False
    except TypeError:
        print("Error: Invalid input type.")
        return False

# Search item: Finds an item by name
def search_item(inventory, name):
    try:
        # Loop through items
        for key, quantity in inventory.items():
            # Case-insensitive match
            if key.lower() == name.lower():
                print(f"Found: {key} (Quantity: {quantity})")
                return (key, quantity)
        print(f"Item {name} not found.")
        return None
    except TypeError:
        print("Error: Invalid input type.")
        return None

# Update item: Changes an item’s quantity
def update_item(inventory, name, quantity):
    try:
        # Check quantity is valid
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        # Find item (case-insensitive)
        for key in inventory:
            if key.lower() == name.lower():
                inventory[key] = quantity
                print(f"Updated {key} to quantity {quantity}.")
                return True
        print(f"Item {name} not found.")
        return False
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return False

# Clear inventory: Removes all items
def clear_inventory(inventory):
    try:
        # Check if already empty
        if not inventory:
            print("Inventory is already empty.")
            return False
        # Clear dictionary
        inventory.clear()
        print("Inventory cleared.")
        return True
    except TypeError:
        print("Error: Invalid inventory data.")
        return False

# Find low stock items: Lists items below a threshold
def find_low_stock(inventory, threshold):
    try:
        # Validate threshold
        if not isinstance(threshold, int) or threshold < 0:
            raise ValueError("Threshold must be a non-negative number.")
        # Collect low stock items
        low_stock = []
        for name, quantity in inventory.items():
            if quantity <= threshold:
                low_stock.append((name, quantity))
        # Print results
        if not low_stock:
            print(f"No items with quantity at or below {threshold}.")
        else:
            print(f"\nLow stock items (quantity <= {threshold}):")
            for i, (name, quantity) in enumerate(low_stock, 1):
                print(f"{i}. {name} (Quantity: {quantity})")
        return low_stock
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return []

# Save inventory: Writes dictionary to inventory.json
def save_inventory(inventory, filename="inventory.json"):
    try:
        # Open file in write mode
        with open(filename, "w") as file:
            # Write dictionary as JSON with indentation
            json.dump(inventory, file, indent=4)
        print(f"Inventory saved to {filename}.")
        return True
    except IOError as e:
        print(f"Error saving inventory: {e}")
        return False
    except TypeError as e:
        print(f"Error: Invalid inventory data: {e}")
        return False

# Count items: Summarizes total items and quantities
# Task 3: Complete this function
def count_items(inventory):
    try:
        # TODO (Task 3): Count unique items and total quantity
        # Hint: Use len(inventory) for number of items
        # Hint: Use sum(inventory.values()) for total quantity
        # Steps:
        # 1. Get number of items
        # 2. Get sum of quantities
        # 3. Print summary: "Inventory summary: X unique items, total quantity: Y"
        # 4. Return tuple (num_items, total_quantity)
        # Example: {"Apple": 5, "Banana": 3} -> Print "2 unique items, total quantity: 8", return (2, 8)
        # --- Your code here ---
        
        # Placeholder to avoid errors
        print("Inventory summary: 0 unique items, total quantity: 0")
        return (0, 0)
    except TypeError as e:
        print(f"Error counting items: {e}")
        return (0, 0)
