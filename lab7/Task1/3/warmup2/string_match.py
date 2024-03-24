def string_match(a, b):
    # Initialize a counter to keep track of matching substrings
    count = 0
    
    # Determine the length of the shorter string
    length = min(len(a), len(b))
    
    # Iterate over the length of the shorter string - 1 (to avoid index out of range)
    for i in range(length - 1):
        # Check if the substring of length 2 at position i in both strings are equal
        if a[i:i+2] == b[i:i+2]:
            count += 1
    
    return count

# Test cases
print(string_match('xxcaazz', 'xxbaaz'))  # Output: 3
print(string_match('abc', 'abc'))         # Output: 2
print(string_match('abc', 'axc'))         # Output: 0
