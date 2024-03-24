def string_bits(str):
    return str[::2]

# Test cases
print(string_bits('Hello'))  # Output: 'Hlo'
print(string_bits('Hi'))  # Output: 'H'
print(string_bits('Heeololeo'))  # Output: 'Hello'
