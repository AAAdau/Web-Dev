def love6(a, b):
    # Check if either a or b is 6, or if their sum or difference is 6
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6

# Test cases
print(love6(6, 4))   # Output: True
print(love6(4, 5))   # Output: False
print(love6(1, 5))   # Output: True
