available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineaple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"sorry, we dont have {requested_topping}")

print("\nFinished making your pizza")