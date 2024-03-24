def end_other(a, b):
    # Convert both strings to lowercase
    a_lower = a.lower()
    b_lower = b.lower()
    
    # Check if one string is a suffix of the other
    return a_lower.endswith(b_lower) or b_lower.endswith(a_lower)

# Test cases
print(end_other('Hiabc', 'abc'))    # Output: True
print(end_other('AbC', 'HiaBc'))     # Output: True
print(end_other('abc', 'abXabc'))    # Output: True
