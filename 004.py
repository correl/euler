def palindrome():
    palindromes = {}
    for i in range(999, 99, -1):
        for ii in range(999,99, -1):
            result = str(i * ii)
            if result == result[::-1]:
                palindromes[i * ii] = [i, ii]
    p = sorted(palindromes.keys(), reverse=True)[0]
    print 'Palindrome: {0}x{1}: {2}'.format(palindromes[p][0], palindromes[p][1], p)

palindrome()
