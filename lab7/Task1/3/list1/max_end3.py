def max_end3(nums):
    # Find the maximum value between the first and last elements
    max_value = max(nums[0], nums[-1])
    # Set all elements of the array to the maximum value
    return [max_value, max_value, max_value]

# Test cases
print(max_end3([1, 2, 3]))    # Output: [3, 3, 3]
print(max_end3([11, 5, 9]))   # Output: [11, 11, 11]
print(max_end3([2, 11, 3]))   # Output: [3, 3, 3]
