"""
Program to demonstrate the use of numpy library in python

import numpy as np

numbers = np.array([10,20,30,40,50])

print(numbers)"""

"""
Program to demonstrate the use of dtype and vectorization in python

import numpy as np

marks = np.array([78,85,91,67,95])

print(marks)
print(type(marks))
print(marks.dtype)

"""

"""
Program to demonstrate the use of 2d arrays in python
import numpy as np

image = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(image[0,1])
"""

"""
#Reverse a list 

list1=[10,20,30,40,50]
for i in range(len(list1)-1,-1,-1):
    print(list1[i])
    
"""

"""
#Program to find the maximum number in a list
numbers = [45, 23, 98, 67, 12]
max=numbers[0]
for i in numbers:
    if i>max:
        max=i
print("The maximum number is:", max)
"""

"""
program to find the second maximum number in a list

numbers = [45, 23, 98, 67, 12]
max=numbers[0]
second_max=numbers[0]
for i in numbers:
    if i>max:
        second_max=max
        max=i
    elif i>second_max and i!=max:
        second_max=i
print("The second maximum number is:", second_max)
"""
"""
program to count the number of odd and even numbers in a list
numbers = [12,15,20,23,44,55,66]
odd=[]
even=[]
for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Number of odd numbers:", len(odd))
print("Number of even numbers:", len(even))
"""

"""
Program to count the number of TB, Normal and Pneumonia cases in a list

labels = [
    "TB",
    "Normal",
    "TB",
    "Pneumonia",
    "Normal",
    "TB"
]

tb_count = 0
normal_count = 0    
pneumonia_count = 0

for label in labels:
    if label == "TB":
        tb_count += 1
    elif label == "Normal":
        normal_count += 1
    elif label == "Pneumonia":
        pneumonia_count += 1

print(f"TB Count: {tb_count}")
print(f"Normal Count: {normal_count}")
print(f"Pneumonia Count: {pneumonia_count}")

"""

numbers = [10,20,30,20,10,40,50]
removed = []
for i in numbers:
    if i not in removed:
        removed.append(i)
print(removed)