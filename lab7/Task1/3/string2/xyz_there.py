def xyz_there(s):
    for i in range(len(s)):
        if s[i:i+3] == 'xyz' and (i == 0 or s[i-1] != '.'):
            return True
    return False

# Test cases
print(xyz_there('abcxyz'))     # Output: True
print(xyz_there('abc.xyz'))    # Output: False
print(xyz_there('xyz.abc'))    # Output: True
