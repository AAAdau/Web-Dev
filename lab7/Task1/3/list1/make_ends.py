def make_ends(nums):
    # Create a new list containing the first and last elements of the input array
    return [nums[0], nums[-1]]

# Test cases
print(make_ends([1, 2, 3]))        # Output: [1, 3]
print(make_ends([1, 2, 3, 4]))     # Output: [1, 4]
print(make_ends([7, 4, 6, 2]))     # Output: [7, 2]
