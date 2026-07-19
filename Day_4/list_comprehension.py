# =====================================
# Day 4 - List Comprehensions
# =====================================

# Normal Loop

numbers = []

for i in range(1, 6):
    numbers.append(i * i)

print(numbers)

# List Comprehension

numbers = [i * i for i in range(1, 6)]

print(numbers)

# Even Numbers

even = [i for i in range(1, 11) if i % 2 == 0]

print(even)

# Odd Numbers

odd = [i for i in range(1, 11) if i % 2 != 0]

print(odd)

# Conditional List Comprehension

result = [i if i % 2 == 0 else 0 for i in range(1, 11)]

print(result)

# Convert to Uppercase

names = ["jacob", "john", "david"]

upper = [name.upper() for name in names]

print(upper)