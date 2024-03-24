def first_two(str):
    # Return the first two characters if the string length is 2 or more
    if len(str) >= 2:
        return str[:2]
    # Otherwise, return the string as it is
    else:
        return str

# Test cases
print(first_two('Hello'))    # Output: 'He'
print(first_two('abcdefg'))  # Output: 'ab'
print(first_two('ab'))       # Output: 'ab'
print(first_two('X'))        # Output: 'X'
print(first_two(''))         # Output: ''
