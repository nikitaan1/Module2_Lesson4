import random

items_list = ["Bike", "Car", "Motorcycle", "Scooter", "Boat", "Airplane"]

selection = random.choice(items_list)
user_selection = input("Select the right transportation: ")

if selection == user_selection:
    print(f"You made the right choice {selection} and {user_selection}")


else:
    print(f"Try again the right choice was {selection}")
