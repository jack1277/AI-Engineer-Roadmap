"""
Program to take user input and display it in a formatted way

Name=input("Enter Your Name : ")
Age=int(input("Enter Your Age : "))
Experience=int(input("Enter Your Experience(Years) : "))
Programming_Language=input("Enter your Programming Language: ")

print(f"Hello {Name}")
print(f"Age : {Age}")
print(f"Experience : {Experience} Years")
print(f"Favourite Language: {Programming_Language}")


"""
"""
Program to display the disease labels for given images
labels=[
    "Normal",
    "Pneumonia",
    "TB",
    "Normal",
    "Pneumonia"
]

for i,disease in enumerate(labels):
    print(f"Image {i+1} -> {disease}")
   
"""
"""
Program to count the number of images for each disease label

labels=[
    "Normal",
    "Pneumonia",
    "TB",
    "Normal",
    "Pneumonia"
]
count={}
for disease in labels:
    if disease in count:
        count[disease]+=1
    else:
        count[disease]=1
for disease,total in count.items():
    print(f"{disease} : {total}")
    
"""
"""
Program to compare actual and predicted disease labels and count correct and wrong predictions

actual = [
    "Normal",
    "TB",
    "Pneumonia",
    "Normal",
    "TB"
]

predicted = [
    "Normal",
    "Normal",
    "Pneumonia",
    "Normal",
    "TB"
]

correct=0
wrong=0

for act,pred in zip(actual,predicted):
    if act==pred:
        correct+=1
    else:
        wrong+=1

print(f"Correct Predictions : {correct}")
print(f"Wrong Predictions : {wrong}")

"""
"""
Program to take user input for actual and predicted disease labels and display if the prediction is correct or wrong

actual=input("Enter Actual Disease : ").lower()
predicted=input("Enter Predicted Disease : ").lower()

if actual == predicted:
    print("Correct Prediction")
else:
    print("Wrong Prediction")
    
"""
"""
Program to generate a random prediction score between 66 and 99

import random
print(f"Prediction Score: {random.randint(66,99)}")

"""