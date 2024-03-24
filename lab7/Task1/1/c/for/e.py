x = int(input())

x_str = str(x)

sum_of_digits = sum(int(digit) for digit in x_str)

print(sum_of_digits)
