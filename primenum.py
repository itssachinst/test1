def is_prime(number):
    if number <= 1:
        return False
    # Check for divisibility from 2 to the square root of the number
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            print(f"{number} is divisible by {divisor}")
            return False
    return True


# Example usage
num = input()
if is_prime(int(num)):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
