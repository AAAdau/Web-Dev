def array123(nums):
    # Iterate through the array and check for the sequence 1, 2, 3
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False

# Test cases
print(array123([1, 1, 2, 3, 1]))  # Output: True
print(array123([1, 1, 2, 4, 1]))  # Output: False
print(array123([1, 1, 2, 1, 2, 3]))  # Output: True
