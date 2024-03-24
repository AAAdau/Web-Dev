def count_code(str):
    count = 0
    for i in range(len(str) - 3):
        if str[i:i+2] == 'co' and str[i+3] == 'e':
            count += 1
    return count

# Test cases
print(count_code('aaacodebbb'))  # Output: 1
print(count_code('codexxcode'))   # Output: 2
print(count_code('cozexxcope'))   # Output: 2
