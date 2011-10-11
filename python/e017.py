"""How many letters would be needed to write all the numbers in words from 1 to 1000?

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

NUMBERS = [
    '',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]
TENS = [
    'n/a',
    'n/a',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
]
TEENS = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
]

def format(n):
    s = []
    if n // 1000:
        s.append(NUMBERS[n // 1000] + ' thousand')
    n = n % 1000
    if n // 100:
        s.append(NUMBERS[n // 100] + ' hundred')
    nn = n % 100
    if n // 100 and nn:
        s.append('and')
    if nn // 10:
        if nn < 20:
            s.append(TEENS[nn % 10])
        else:
            s.append(TENS[nn // 10] + ('-' + NUMBERS[nn % 10] if nn % 10 else ''))
    else:
        s.append(NUMBERS[nn % 10])
    return ' '.join(s)

def main():
    chars = []
    for i in range(1, 1001):
        chars = chars + list(format(i).replace(' ', '').replace('-', ''))
    print 'Chars:', len(chars)

if __name__ == '__main__':
    main()
