motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# modifying elements in a list
motorcycles[0] = 'ducati'
print(motorcycles)

# adding elements to a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append("ducati")
print(motorcycles)

# inserting elements to a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# removing elements to a list

del motorcycles[0] # del statement
print(motorcycles)

popped_motorcycles = motorcycles.pop() # pop last element
print(motorcycles)
print(popped_motorcycles)

print(motorcycles.pop(0)) # pop element from any position

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] # remove by value
print(motorcycles.remove('ducati'))
