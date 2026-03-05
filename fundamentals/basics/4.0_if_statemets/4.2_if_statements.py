# simple if statement
age = 19
if age >= 18:
    print("you are old enough to vote")

# if-else statements
age = 17
if age >= 18:
    print("you are old enough to vote")
else:
    print("sorry you are too young to vote")

# the if-elif-else chain
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"your admission cost is ${price}")

# testing multiple conditions
requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print("Adding mushrooms")
elif "pepperoni" in requested_toppings:
    print("Adding pepperoni")
elif "extra cheese" in requested_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza!")
