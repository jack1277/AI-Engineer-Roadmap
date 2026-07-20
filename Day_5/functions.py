# ==============================
# DAY 5 - FUNCTIONS
# ==============================

# Function Definition and Function Call

def greet():
    print("Hello, Welcome to Python!")

greet()

# ----------------------------------

# Function with Parameters

def add(a, b):
    return a + b

print("Sum:", add(10, 20))

# ----------------------------------

# Difference between print() and return()

def using_print():
    print("This uses print")

def using_return():
    return "This uses return"

using_print()
print(using_return())

# ----------------------------------

# Local Variable

def local_variable():
    x = 100
    print("Local Variable:", x)

local_variable()

# ----------------------------------

# Global Variable

x = 50

def global_variable():
    print("Global Variable:", x)

global_variable()

# ----------------------------------

# Multiple Return Values

def calculations(a, b):
    return a + b, a - b

sum_result, difference = calculations(20, 10)

print("Sum:", sum_result)
print("Difference:", difference)