def left2(str):
    # Concatenate substring starting from the third character with the first two characters
    return str[2:] + str[:2]

# Test cases
print(left2('Hello'))  # Output: 'lloHe'
print(left2('java'))   # Output: 'vaja'
print(left2('Hi'))     # Output: 'Hi'
