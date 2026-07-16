def second_largest(numbers):
    max_num=numbers[0]
    second_max=float('-inf') 
    for i in numbers:
        if i>max_num:
            second_max=max_num
            max_num=i
        elif i>second_max and i!=max_num:
            second_max=i
    return second_max
    
print(second_largest([45, 23, 98, 67, 12]))