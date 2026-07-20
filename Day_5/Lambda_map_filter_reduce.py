# ==============================
# DAY 5 - LAMBDA, MAP, FILTER, REDUCE
# ==============================

from functools import reduce

# -----------------------------
# Lambda Function
# -----------------------------

square = lambda x: x ** 2
print("Square:", square(5))

maximum = lambda a, b: a if a > b else b
print("Maximum:", maximum(10, 20))

# -----------------------------
# map()
# -----------------------------

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

multiply = list(map(lambda x: x * 10, numbers))
print("Multiply by 10:", multiply)

# -----------------------------
# filter()
# -----------------------------

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

greater_than_three = list(filter(lambda x: x > 3, numbers))
print("Greater than 3:", greater_than_three)

# -----------------------------
# reduce()
# -----------------------------

sum_all = reduce(lambda a, b: a + b, numbers)
print("Sum:", sum_all)

product = reduce(lambda a, b: a * b, numbers)
print("Product:", product)

largest = reduce(lambda a, b: a if a > b else b, numbers)
print("Largest:", largest)

# -----------------------------
# Combining filter() and map()
# -----------------------------

result = list(
    map(
        lambda x: x * 10,
        filter(lambda x: x % 2 == 0, numbers)
    )
)

print("Even numbers multiplied by 10:", result)