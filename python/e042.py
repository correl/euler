# -*- coding: utf-8 -*-
"""How many triangle words does the list of common English words contain?

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (p042/words.txt), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

import csv

def triangle_generator():
    i = 0
    n = 0
    while True:
        i = i + 1
        n = n + i
        yield n

def main():
    word_list = []
    reader = csv.reader(open('p042/words.txt'), delimiter=',', quotechar='"')
    for row in reader:
        word_list = word_list + row
    word_list = sorted(word_list)
    
    total = 0
    words = {}
    for word in word_list:
        score = 0
        for c in word:
            score = score + (ord(c) - 64)
        words[word] = score

    max_score = max(words.values())
    triangles = []
    for i in triangle_generator():
        if i > max_score:
            break
        triangles.append(i)
    for (word, score) in words.iteritems():
        if score in triangles:
            total = total + 1
    print 'Total:', total

if __name__ == '__main__':
    main()
