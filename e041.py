"""What is the largest n-digit pandigital prime that exists?

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from e007 import is_prime
from e035 import permutations

def pandigital_prime_generator(n):
  if n > 7:
    raise Exception('Invalid pandigital prime length')
  for end in [3, 7, 9]:
    digits = range(1, n + 1)
    if end not in digits:
      continue
    digits.remove(end)
    for start in sorted(permutations(digits, len(digits)), reverse=True):
      number = int(''.join([str(i) for i in start] + [str(end)]))
      if is_prime(number):
        yield number

def main():
  for len in range(7, 2, -1):
    for n in sorted(pandigital_prime_generator(len), reverse=True):
      print 'Pandigital Prime:', n
      return

if __name__ == '__main__':
  main()
