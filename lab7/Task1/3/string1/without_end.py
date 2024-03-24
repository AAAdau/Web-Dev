def without_end(str):
    # Return the substring from the second character to the second-to-last character
    return str[1:-1]

# Test cases
print(without_end('Hello'))    # Output: 'ell'
print(without_end('java'))     # Output: 'av'
print(without_end('coding'))   # Output: 'odin'
