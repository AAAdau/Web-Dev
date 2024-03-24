def near_hundred(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)

# Test cases
print(near_hundred(93)) # Output: True
print(near_hundred(90)) # Output: True
print(near_hundred(89)) # Output: False
