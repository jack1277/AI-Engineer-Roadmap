# =====================================
# Day 4 - Interview Practice
# =====================================

# Q1
a = (5)
b = (5,)

print(type(a))
print(type(b))

# ----------------------------

# Q2

empty_dict = {}
empty_set = set()

print(type(empty_dict))
print(type(empty_set))

# ----------------------------

# Q3

student = {
    "name": "Jacob",
    "age": 21
}

print(student.get("salary"))
print(student.get("salary", 0))

# ----------------------------

# Q4

python_students = {"Jacob", "John"}
ai_students = {"Jacob", "Mary"}

print("Union:", python_students | ai_students)
print("Intersection:", python_students & ai_students)
print("Difference:", python_students - ai_students)

# ----------------------------

# Q5

square = [i * i for i in range(1, 6)]

print(square)

# ----------------------------

# Q6

even = [i for i in range(1, 11) if i % 2 == 0]

print(even)

# ----------------------------

# Q7

result = [i if i % 2 == 0 else 0 for i in range(1, 6)]

print(result)