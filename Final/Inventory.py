class Inventory:
    def __init__(self):
        self.item = ''
        self.quantity = 0

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity


shirt_inventory = Inventory()
item = shirt_inventory.set_item("Shirts")
quantity = shirt_inventory.set_quantity(5)
shirt_inventory.get_item()
shirt_inventory.get_quantity()


class InventoryMessage(Inventory):
    def __init__(self):
        super().__init__()
        Inventory.quantity = 0
        Inventory.item = ''

    quantity = shirt_inventory.set_quantity(5)
    Inventory.get_quantity(shirt_inventory)

    def get_inventory_message(self, item):
        if Inventory.quantity > 0:
            print(f"{item} In Stock")
        else:
            print(f"{item} Out of Stock")
