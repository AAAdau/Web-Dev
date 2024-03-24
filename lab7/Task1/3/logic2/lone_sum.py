def lone_sum(a, b, c):
    # Check if all three values are the same
    if a == b == c:
        return 0
    # Check each value individually and add it to the sum if it is different from the other two
    elif a != b != c != a:
        return a + b + c
    elif a == b:
        return c
    elif b == c:
        return a
    elif a == c:
        return b

# Test cases
print(lone_sum(1, 2, 3))   # Output: 6
print(lone_sum(3, 2, 3))   # Output: 2
print(lone_sum(3, 3, 3))   # Output: 0
