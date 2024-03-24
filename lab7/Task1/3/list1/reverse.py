def reverse3(nums):
    # Create a new list with elements in reverse order
    return [nums[2], nums[1], nums[0]]

# Test cases
print(reverse3([1, 2, 3]))    # Output: [3, 2, 1]
print(reverse3([5, 11, 9]))   # Output: [9, 11, 5]
print(reverse3([7, 0, 0]))    # Output: [0, 0, 7]
