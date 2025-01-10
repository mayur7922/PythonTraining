class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if quantity <= 0:
            raise ValueError("Quantity to add must be positive.")
        
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

        return f"Added {quantity} of {item_name}. Current stock: {self.items[item_name]}"

    def remove_item(self, item_name, quantity):

        if quantity <= 0:
            raise ValueError("Quantity to remove must be positive.")
        
        if item_name not in self.items:
            raise ValueError(f"Item {item_name} not found in inventory.")
        
        if self.items[item_name] < quantity:
            raise ValueError(f"Insufficient stock for {item_name}. Current stock: {self.items[item_name]}")
        
        self.items[item_name] -= quantity
        if self.items[item_name] == 0:
            del self.items[item_name]

        return f"Removed {quantity} of {item_name}. Current stock: {self.items.get(item_name, 0)}"

    def query_item(self, item_name):
        return f"Current stock of {item_name}: {self.items.get(item_name, 'Item not found')}"

if __name__ == "__main__":
    try:
        inventory = Inventory()

        print(inventory.add_item("apple", 10))
        print(inventory.add_item("banana", 20)) 

        print(inventory.query_item("apple")) 
        print(inventory.query_item("orange"))  

        print(inventory.remove_item("apple", 5)) 
        print(inventory.remove_item("banana", 25)) 
    except ValueError as e:
        print(e)  
