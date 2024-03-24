def round10(num):
    # Calculate the remainder when dividing num by 10
    remainder = num % 10
    # Round up to the next multiple of 10 if the remainder is 5 or more
    if remainder >= 5:
        return num + (10 - remainder)
    # Round down to the previous multiple of 10 if the remainder is less than 5
    else:
        return num - remainder

def round_sum(a, b, c):
    # Round each number using the round10 helper function
    rounded_a = round10(a)
    rounded_b = round10(b)
    rounded_c = round10(c)
    # Return the sum of the rounded numbers
    return rounded_a + rounded_b + rounded_c

# Test cases
print(round_sum(16, 17, 18))  # Output: 60
print(round_sum(12, 13, 14))  # Output: 30
print(round_sum(6, 4, 4))      # Output: 10
