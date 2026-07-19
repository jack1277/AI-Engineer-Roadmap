# =====================================
# Day 4 - Set Practice
# =====================================

numbers = {10, 20, 30, 20, 10, 40}

print("Set:", numbers)

# Add
numbers.add(50)

# Remove
numbers.remove(20)

# Discard (No error if element absent)
numbers.discard(100)

print(numbers)

python_students = {"Jacob", "John", "David"}
ai_students = {"Jacob", "Mary", "David"}

print("\nUnion")
print(python_students | ai_students)

print("\nIntersection")
print(python_students & ai_students)

print("\nDifference")
print(python_students - ai_students)

print("\nMembership")

if "Jacob" in python_students:
    print("Jacob is enrolled.")

# Empty Set
empty = set()

print(type(empty))