inventory = {}

def add_product(name, quantity):
    inventory[name] = quantity

def update_quantity(name, quantity):
    if name in inventory:
        inventory[name] = quantity
    else:
        print("Product not found")

def remove_product(name):
    if name in inventory and inventory[name] == 0:
        del inventory[name]
        print("Product removed")
    else:
        print("Product cannot be removed")

def highest_stock():
    if inventory:
        product = max(inventory, key=inventory.get)
        print("Product with highest stock:", product)
        print("Quantity:", inventory[product])

def display_inventory():
    print("Inventory:", inventory)
    print("Total unique products:", len(inventory))


add_product("Pen", 50)
add_product("Notebook", 30)
add_product("Pencil", 70)

update_quantity("Notebook", 40)

inventory["Pen"] = 0
remove_product("Pen")

display_inventory()
highest_stock()
