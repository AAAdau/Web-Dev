def first_half(str):
    # Calculate the index at which to stop
    half_length = len(str) // 2
    # Return the substring from the beginning of the string up to half of its length
    return str[:half_length]

# Test cases
print(first_half('WooHoo'))      # Output: 'Woo'
print(first_half('HelloThere'))   # Output: 'Hello'
print(first_half('abcdef'))      # Output: 'abc'
