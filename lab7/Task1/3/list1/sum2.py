def sum2(nums):
    # If array length is less than 2, sum up all elements in the array
    if len(nums) < 2:
        return sum(nums)
    # Otherwise, sum up the first two elements
    else:
        return nums[0] + nums[1]

# Test cases
print(sum2([1, 2, 3]))       # Output: 3
print(sum2([1, 1]))          # Output: 2
print(sum2([1, 1, 1, 1]))    # Output: 2
print(sum2([5]))             # Output: 5
print(sum2([]))              # Output: 0
