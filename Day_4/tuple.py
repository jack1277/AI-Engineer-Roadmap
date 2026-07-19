# =====================================
# Day 4 - Tuple Practice
# =====================================

# Creating tuples
numbers = (10, 20, 30, 40)
print("Tuple:", numbers)

# Single element tuple
single = (5,)
print(type(single))

# Tuple Packing
student = "Jacob", 21, "AI & ML"
print(student)

# Tuple Unpacking
name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)

# Extended Unpacking
a, *b = (10, 20, 30, 40)

print("a =", a)
print("b =", b)

# Tuple Methods
marks = (95, 90, 95, 88, 95)

print("Count of 95:", marks.count(95))
print("Index of 88:", marks.index(88))

# Tuple Immutability
# numbers[0] = 100   # Uncomment to see TypeError