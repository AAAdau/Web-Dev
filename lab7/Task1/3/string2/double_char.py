def double_char(str):
    result = ''
    for char in str:
        result += char * 2
    return result

# Test cases
print(double_char('The'))        # Output: 'TThhee'
print(double_char('AAbb'))       # Output: 'AAAAbbbb'
print(double_char('Hi-There'))   # Output: 'HHii--TThheerree'
