def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result += str[:i+1]
    return result

# Test cases
print(string_splosion('Code'))  # Output: 'CCoCodCode'
print(string_splosion('abc'))  # Output: 'aababc'
print(string_splosion('ab'))  # Output: 'aab'
