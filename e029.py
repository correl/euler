MAX = 100

numbers = []

for i in range(2, MAX + 1):
    for ii in range(2, MAX + 1):
        n = i**ii
        if n not in numbers:
            numbers.append(n)
print len(numbers)
