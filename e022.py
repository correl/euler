import csv

names = []
reader = csv.reader(open('p022/names.txt'), delimiter=',', quotechar='"')
for row in reader:
    names = names + row
names = sorted(names)
total = 0

i = 1
for name in names:
    score = 0
    for c in name:
        score = score + (ord(c) - 64)
    score = i * score
    total = total + score
    i = i + 1

print 'Total:', total