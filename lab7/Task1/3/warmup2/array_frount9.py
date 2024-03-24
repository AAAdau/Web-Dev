def array_front9(nums):
    # Check if 9 is in the first 4 elements of the array
    return 9 in nums[:4]

# Test cases
print(array_front9([1, 2, 9, 3, 4]))  # Output: True
print(array_front9([1, 2, 3, 4, 9]))  # Output: False
print(array_front9([1, 2, 3, 4, 5]))  # Output: False
