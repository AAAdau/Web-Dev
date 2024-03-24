def close_far(a, b, c):
    # Check condition 1
    if abs(b - a) <= 1 and abs(c - a) >= 2 and abs(c - b) >= 2:
        return True
    # Check condition 2
    if abs(c - a) <= 1 and abs(b - a) >= 2 and abs(b - c) >= 2:
        return True
    return False

# Test cases
print(close_far(1, 2, 10))  # Output: True
print(close_far(1, 2, 3))   # Output: False
print(close_far(4, 1, 3))   # Output: True
