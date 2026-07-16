def palidrome(text):
    reverse=""
    for i in text:
        reverse=i+reverse
    if reverse==text:
        return "Palindrome"
    else:
        return "Not a Palindrome"
        
text=input("Enter a string: ")
print(palidrome(text))