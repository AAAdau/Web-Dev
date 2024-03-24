def front_times(str, n):
    front = str[:3]
    return front * n

# Test cases
print(front_times('Chocolate', 2))  # Output: 'ChoCho'
print(front_times('Chocolate', 3))  # Output: 'ChoChoCho'
print(front_times('Abc', 3))  # Output: 'AbcAbcAbc'
