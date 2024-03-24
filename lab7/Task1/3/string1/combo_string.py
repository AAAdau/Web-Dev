def combo_string(a, b):
    # Check which string is shorter
    if len(a) < len(b):
        # If a is shorter, concatenate it with b and then with a again
        return a + b + a
    else:
        # If b is shorter, concatenate it with a and then with b again
        return b + a + b

# Test cases
print(combo_string('Hello', 'hi'))   # Output: 'hiHellohi'
print(combo_string('hi', 'Hello'))   # Output: 'hiHellohi'
print(combo_string('aaa', 'b'))      # Output: 'baaab'
