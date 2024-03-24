def array_count9(nums):
    count = 0
    # Iterate through the list and count the occurrences of 9
    for num in nums:
        if num == 9:
            count += 1
    return count

# Test cases
print(array_count9([1, 2, 9]))       # Output: 1
print(array_count9([1, 9, 9]))       # Output: 2
print(array_count9([1, 9, 9, 3, 9])) # Output: 3
