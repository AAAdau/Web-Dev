def middle_way(a, b):
    # Create a new list containing the middle elements of the input arrays
    return [a[1], b[1]]

# Test cases
print(middle_way([1, 2, 3], [4, 5, 6]))    # Output: [2, 5]
print(middle_way([7, 7, 7], [3, 8, 0]))    # Output: [7, 8]
print(middle_way([5, 2, 9], [1, 4, 5]))    # Output: [2, 4]
