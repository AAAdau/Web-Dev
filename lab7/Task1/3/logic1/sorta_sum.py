def sorta_sum(a, b):
    # Calculate the sum of a and b
    total = a + b
    # Check if the sum is in the forbidden range (10 to 19)
    if 10 <= total <= 19:
        return 20
    else:
        return total

# Test cases
print(sorta_sum(3, 4))     # Output: 7
print(sorta_sum(9, 4))     # Output: 20
print(sorta_sum(10, 11))   # Output: 21
