# =====================================
# Day 4 - Dictionary Practice
# =====================================

student = {
    "name": "Jacob",
    "age": 21,
    "course": "AI & ML"
}

print(student)

print("\nKeys")
print(student.keys())

print("\nValues")
print(student.values())

print("\nItems")
print(student.items())

print("\nLoop Through Dictionary")

for key, value in student.items():
    print(key, ":", value)

print("\nUsing get()")

print(student.get("age"))
print(student.get("salary"))
print(student.get("salary", "Not Found"))

print("\nUpdate")

student.update({"age": 22})
student.update({"city": "Coimbatore"})

print(student)

print("\nPop")

student.pop("city")

print(student)