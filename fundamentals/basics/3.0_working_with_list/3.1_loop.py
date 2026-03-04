magicians = ['alice', 'david', 'carolina']
# for loop
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

# range function
for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# more concisely
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# python function
digits = [1, 2, 3, 4, 5, 6, 7]
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)