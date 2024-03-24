def near_ten(num):
    remainder = num % 10
    return remainder <= 2 or remainder >= 8

# Test cases
print(near_ten(12))   # Output: True
print(near_ten(17))   # Output: False
print(near_ten(19))   # Output: True
