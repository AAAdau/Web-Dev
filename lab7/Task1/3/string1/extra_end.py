def extra_end(str):
    # Extract the last two characters of the string
    end = str[-2:]
    # Return the concatenation of the last two characters three times
    return end * 3

# Test cases
print(extra_end('Hello'))  # Output: 'lololo'
print(extra_end('ab'))     # Output: 'ababab'
print(extra_end('Hi'))     # Output: 'HiHiHi'
