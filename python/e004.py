"""Find the largest palindrome made from the product of two 3-digit numbers.

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def palindrome():
    palindromes = {}
    for i in range(999, 99, -1):
        for ii in range(999,99, -1):
            result = str(i * ii)
            if result == result[::-1]:
                palindromes[i * ii] = [i, ii]
    p = sorted(palindromes.keys(), reverse=True)[0]
    print 'Palindrome: {0}x{1}: {2}'.format(palindromes[p][0], palindromes[p][1], p)
def main():
    palindrome()

if __name__ == '__main__':
    main()
