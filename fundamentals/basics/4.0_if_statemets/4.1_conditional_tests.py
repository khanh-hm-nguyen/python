# checking for equality
car = "bmw"
print(car == "bmw")
print(car == "audi")

# case sensitive
car = "Audi"
print(car == "audi")
print(car.lower() == "audi")

# checking for inequality
requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies")

#numerical comparisons
age = 18
print(age == 50)

answer = 17
if answer != 42:
    print("that is not the correct answer. please try again!")

#checking multiple conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >=21)
age_1 = 23
print(age_0 >= 21 and age_1 >=21)

#checking whether a value is in a list
requested_topping = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_topping)
print("pepperoni" in requested_topping)

banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")

# boolean expressions
game_active = True
can_edit = False
