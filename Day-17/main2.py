class Restaurant:

    def __init__(self, name, cuisine, served):
        self.name = name
        self.cuisine = cuisine
        self.served = 0

    def describe_restaurant(self):
        print(f"Welcome to the {self.name} Restaurant")
        print(f"We serve {self.cuisine} type of food")

    def open_restaurant(self):
        print("Restaurant is OPEN!")

restaurant = Restaurant("Ahmet", "Japan", 10)
restaurant.served = 10
print(f"{restaurant.served} number ")