def largest(numbers):
    largest=numbers[0]
    for i in numbers:
        if i>largest:
            largest=i
    return largest

print(largest([45, 23, 98, 67, 12]))