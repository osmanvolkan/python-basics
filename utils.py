def find_maximum(numbers):
    max=numbers[0]
    for i in numbers:
        if i>max:
            max=i
    return max