"""Develop a method to express Roman numerals in minimal form.

The rules for writing Roman numerals allow for many ways of writing each number (see FAQ: Roman Numerals). However, there is always a "best" way of writing a particular number.

For example, the following represent all of the legitimate ways of writing the number sixteen:
    IIIIIIIIIIIIIIII
    VIIIIIIIIIII
    VVIIIIII
    XIIIIII
    VVVI
    XVI

The last example being considered the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (p089/roman.txt), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; that is, they are arranged in descending units and obey the subtractive pair rule (see FAQ for the definitive rules for this problem).

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
"""

ROMAN_NUMERALS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman_to_decimal(s):
    # Read in roman digits in reverse
    last = None
    total = 0
    for c in s[::-1]:
        val = ROMAN_NUMERALS[c]
        if last and val < last:
            total = total - val
        else:
            total = total + val
            last = val
    return total

def decimal_to_roman(n):
    roman = ''
    lookup = dict([(v, k) for (k, v) in ROMAN_NUMERALS.iteritems()])
    values = sorted(ROMAN_NUMERALS.values())
    total = 0
    subtracted = False
    for i in xrange(len(values)):
        val = values[i]
        if val == max(values):
            count = n // val
            roman = (lookup[val] * count) + roman
        else:
            nn = (n - total) % values[i + 1]
            count = nn // val
            if count > 3:
                roman = lookup[val] + lookup[values[i + 2]] + roman
                subtracted = True
            else:
                if count and subtracted:
                    count = count - 1
                subtracted = False
                roman = (lookup[val] * count) + roman
            total = total + nn
    return roman

def main():
    saved = 0
    with open('p089/roman.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            old = line.strip()
            new = decimal_to_roman(roman_to_decimal(old))
            print roman_to_decimal(old), old, new
            saved = saved + (len(old) - len(new))
    print 'Saved:', saved

if __name__ == '__main__':
    main()
