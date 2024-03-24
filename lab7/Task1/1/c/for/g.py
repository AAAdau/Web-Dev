x = int(input())

min_divisor = None

for divisor in range(2, int(x ** 0.5) + 1):
    if x % divisor == 0:
        min_divisor = divisor
        break

if min_divisor is None:
    min_divisor = x

print(min_divisor)
