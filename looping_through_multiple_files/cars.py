available_toppings = ['mushrooms', 'ham', 'pineapple']
requested_toppings = ['mushrooms', 'ham', 'french fries']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry we don't offer {requested_topping}")

print("We've finished making your pizza!")
