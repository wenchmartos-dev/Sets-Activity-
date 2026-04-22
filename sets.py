# Set Activities

# Activity 1: Remove Duplicates
numbers = [1, 2, 2, 3, 4, 5]
unique = set(numbers)
print(unique)

# Activity 2: Add and Remove
fruits = {"apple", "banana"}
fruits.add("avocado")
fruits.remove("banana")
print(fruits)

# Activity 3: Set Operations
A = {1, 2, 3}
B = {3, 4, 5}
print(A | B)   # union
print(A & B)   # intersection

# Activity 4: Common Students
classA = {"Juan", "Maria", "Joseph"}
classB = {"Bitoy", "Budoy", "Elay"}
print(classA & classB)  # both
print(classA | classB)  # all
