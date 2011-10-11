"""What is the total of all the name scores in the file of first names?

Using names.txt (p022/names.txt), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
"""

import csv

def main():
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

if __name__ == '__main__':
    main()
