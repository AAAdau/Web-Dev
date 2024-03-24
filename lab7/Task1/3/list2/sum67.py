def sum67(nums):
    total = 0
    in_section = False  # Flag to indicate if we are currently in a section to ignore
    for num in nums:
        if num == 6:
            in_section = True
            continue
        elif num == 7 and in_section:
            in_section = False
            continue
        elif not in_section:
            total += num
    return total

# Test cases
print(sum67([1, 2, 2]))  # Output: 5
print(sum67([1, 2, 2, 6, 99, 99, 7]))  # Output: 5
print(sum67([1, 1, 6, 7, 2]))  # Output: 4
