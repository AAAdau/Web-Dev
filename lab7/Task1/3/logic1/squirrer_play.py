def squirrel_play(temperature, is_summer):
    # Check if it's summer and the temperature is between 60 and 100 (inclusive),
    # or if it's not summer and the temperature is between 60 and 90 (inclusive)
    return (is_summer and 60 <= temperature <= 100) or (not is_summer and 60 <= temperature <= 90)

# Test cases
print(squirrel_play(70, False))   # Output: True
print(squirrel_play(95, False))   # Output: False
print(squirrel_play(95, True))    # Output: True
