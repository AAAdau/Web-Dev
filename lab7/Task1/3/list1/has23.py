def has23(nums):
    # Check if 2 or 3 is present in the array
    return 2 in nums or 3 in nums

# Test cases
print(has23([2, 5]))   # Output: True
print(has23([4, 3]))   # Output: True
print(has23([4, 5]))   # Output: False
