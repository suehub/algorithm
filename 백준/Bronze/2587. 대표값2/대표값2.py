numbers = []

for _ in range(5):
    numbers.append(int(input()))

numbers = sorted(numbers)

print((sum(numbers)/5).__ceil__())
print(numbers[2])