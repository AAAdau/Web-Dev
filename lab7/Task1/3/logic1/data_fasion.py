def date_fashion(you, date):
    # If either of you has style of 2 or less, return 0 (no)
    if you <= 2 or date <= 2:
        return 0
    # If either of you is very stylish (8 or more), return 2 (yes)
    elif you >= 8 or date >= 8:
        return 2
    # Otherwise, return 1 (maybe)
    else:
        return 1

# Test cases
print(date_fashion(5, 10))  # Output: 2
print(date_fashion(5, 2))   # Output: 0
print(date_fashion(5, 5))   # Output: 1
