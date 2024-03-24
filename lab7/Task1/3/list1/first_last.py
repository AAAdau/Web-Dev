def first_last6(nums):
    # Check if the first or last element of the array is equal to 6
    return nums[0] == 6 or nums[-1] == 6

# Test cases
print(first_last6([1, 2, 6]))         # Output: True
print(first_last6([6, 1, 2, 3]))      # Output: True
print(first_last6([13, 6, 1, 2, 3]))  # Output: False
