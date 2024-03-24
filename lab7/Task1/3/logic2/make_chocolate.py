def make_chocolate(small, big, goal):
    # Calculate the maximum kilos of chocolate we can make using the big bars
    max_big_kilos = big * 5
    # Calculate the remaining goal after using big bars
    remaining_goal = goal - min(goal // 5, big) * 5
    
    # Check if we can make the remaining goal using small bars
    if remaining_goal <= small:
        return remaining_goal
    else:
        return -1

# Test cases
print(make_chocolate(4, 1, 9))   # Output: 4
print(make_chocolate(4, 1, 10))  # Output: -1
print(make_chocolate(4, 1, 7))   # Output: 2
