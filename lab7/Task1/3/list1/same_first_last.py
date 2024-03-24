def same_first_last(nums):
    # Check if the array has a length of 1 or more and if the first element is equal to the last element
    return len(nums) >= 1 and nums[0] == nums[-1]

# Test cases
print(same_first_last([1, 2, 3]))   # Output: False
print(same_first_last([1, 2, 3, 1]))  # Output: True
print(same_first_last([1, 2, 1]))    # Output: True
