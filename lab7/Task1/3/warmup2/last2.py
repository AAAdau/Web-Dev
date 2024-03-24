def last2(str):
    # Check if the string length is less than 2, return 0 in such case
    if len(str) < 2:
        return 0
    
    # Get the last two characters of the string
    end = str[-2:]
    count = 0
    
    # Iterate through the string up to the second to last index
    for i in range(len(str) - 2):
        # Check if the current substring of length 2 matches the end substring
        if str[i:i+2] == end:
            count += 1
    return count

# Test cases
print(last2('hixxhi'))   # Output: 1
print(last2('xaxxaxaxx'))   # Output: 1
print(last2('axxxaaxx'))   # Output: 2
