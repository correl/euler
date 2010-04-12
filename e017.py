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

if __name__ == '__main__':
    chars = []
    for i in range(1, 1001):
        chars = chars + list(format(i).replace(' ', '').replace('-', ''))
    print 'Chars:', len(chars)
