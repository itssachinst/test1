def find_largest(numbers):
    if not numbers:
        return None  # Return None for an empty list

    largest = numbers[0]  # Assume the first number is the largest

    for i in range(len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]

    return largest

# Example usage
my_list = [12, 45, 67, 23, 9, 100]
result = find_largest(my_list)
print("The largest number is:", result)

