message = input("Tell me something, and i will reapeat it back to you: ")
print(message)

#writing clear prompts
prompt = "If you share your name, we can ersonalized the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"Hello, {name}!")

# Using int() to accept numerical input
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

#the modulo operator
number = input("Enter a number, and I'll tell you if it is even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"\nThe number {number} is odd")