# ==============================
# DAY 5 - EXCEPTION HANDLING
# ==============================

# Basic try-except

try:
    number = int(input("Enter a number: "))
    print("Result:", 10 / number)

except:
    print("An error occurred.")

# --------------------------------

# Specific Exceptions

try:
    number = int(input("Enter another number: "))
    print(20 / number)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter a valid integer.")

# --------------------------------

# Multiple Exceptions

try:
    numbers = [10, 20, 30]
    print(numbers[5])

except IndexError:
    print("Index out of range.")

# --------------------------------

# else block

try:
    x = int(input("Enter a value: "))

except ValueError:
    print("Invalid input.")

else:
    print("You entered:", x)

# --------------------------------

# finally block

try:
    print("Opening file...")

except Exception:
    print("Something went wrong.")

finally:
    print("Program execution completed.")