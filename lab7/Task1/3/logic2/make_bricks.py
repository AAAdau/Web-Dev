def make_bricks(small, big, goal):
    # Calculate the total length that can be covered by the big bricks alone
    big_bricks_covered_length = big * 5
    # Determine the remaining length needed after covering with big bricks
    remaining_length = goal - big_bricks_covered_length
    # Check if the remaining length can be covered by the available small bricks
    return remaining_length <= small and remaining_length >= 0

# Test cases
print(make_bricks(3, 1, 8))    # Output: True
print(make_bricks(3, 1, 9))    # Output: False
print(make_bricks(3, 2, 10))   # Output: True
