
inventory = [
    {"name": "Apples", "quantity": 10},
    {"name": "Bananas", "quantity": 5},
    {"name": "Oranges", "quantity": 8}
]

def display_inventory():
    print("\nCurrent Inventory:")
    for item in inventory:
        name = item['name']
        quantity = item['quantity']
        print(name + ": " + str(quantity))

def add_item():
    item_name = input("Enter new item name: ").capitalize()
    
    
    for item in inventory:
        if item['name'] == item_name:
            print("Item already exists.")
            return
    
    quantity = int(input("Enter quantity: "))
    inventory.append({"name": item_name, "quantity": quantity})
    print("Added new item: " + item_name + " with quantity " + str(quantity))

def update_item():
    item_name = input("Enter item name to update: ").capitalize()
    
    for item in inventory:
        if item['name'] == item_name:
            new_quantity = int(input("Enter new quantity: "))
            item['quantity'] = new_quantity
            print("Updated " + item_name + ": new quantity is " + str(item['quantity']))
            return
    
    print("Item not found. ")

def remove_item():
    item_name = input("Enter item name to remove: ").capitalize()
    
    for item in inventory:
        if item['name'] == item_name:
            inventory.remove(item)
            print("Removed item: " + item_name)
            return
    
    print("Item not found..")
    
while True:
    print("\n--- Inventory Management ---")
    print("display")
    print("add")
    print("update")
    print("remove")
    print("exit")
    
    command = input("Enter a command: ").lower()

    if command == "display":
        display_inventory()
    elif command == "add":
        add_item()
    elif command == "update":
        update_item()
    elif command == "remove":
        remove_item()
    elif command == "exit":
        print("Exiting Inventory Management.")
        break
    else:
        print("Invalid command. Please try again.")
