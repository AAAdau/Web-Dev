def front_back(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + s[1:-1] + s[0]

# Test cases
print(front_back('code')) # Output: 'eodc'
print(front_back('a')) # Output: 'a'
print(front_back('ab')) # Output: 'ba'
