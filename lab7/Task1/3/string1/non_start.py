def non_start(a, b):
    # Concatenate substrings of each string starting from the second character
    return a[1:] + b[1:]

# Test cases
print(non_start('Hello', 'There'))  # Output: 'ellohere'
print(non_start('java', 'code'))    # Output: 'avaode'
print(non_start('shotl', 'java'))   # Output: 'hotlava'
