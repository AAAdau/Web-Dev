def diff21(n):
    if n <= 21:
        return abs(21 - n)
    else:
        return abs(21 - n) * 2

# Test cases
print(diff21(19)) # Output: 2
print(diff21(10)) # Output: 11
print(diff21(21)) # Output: 0
