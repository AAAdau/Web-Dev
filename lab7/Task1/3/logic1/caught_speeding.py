def caught_speeding(speed, is_birthday):
    # If it's your birthday, your speed can be 5 higher in all cases
    if is_birthday:
        speed -= 5
    # Check the speed and return the corresponding result
    if speed <= 60:
        return 0
    elif 61 <= speed <= 80:
        return 1
    else:
        return 2

# Test cases
print(caught_speeding(60, False))   # Output: 0
print(caught_speeding(65, False))   # Output: 1
print(caught_speeding(65, True))    # Output: 0
