def not_string(s):
    if s.startswith('not'):
        return s
    else:
        return 'not ' + s

# Test cases
print(not_string('candy')) # Output: 'not candy'
print(not_string('x')) # Output: 'not x'
print(not_string('not bad')) # Output: 'not bad'
