a = int(input())
b = int(input())

even_numbers = []

for num in range(a, b+1):
    if num % 2 == 0:
        even_numbers.append(num)

print(' '.join(map(str, even_numbers)))