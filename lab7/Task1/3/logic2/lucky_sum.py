def lucky_sum(a, b, c):
    # Check if a is 13
    if a == 13:
        return 0
    # Check if b is 13
    elif b == 13:
        return a
    # Check if c is 13
    elif c == 13:
        return a + b
    # If none of the values are 13, return their sum
    else:
        return a + b + c

# Test cases
print(lucky_sum(1, 2, 3))   # Output: 6
print(lucky_sum(1, 2, 13))  # Output: 3
print(lucky_sum(1, 13, 3))  # Output: 1
    