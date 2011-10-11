"""By analysing a user's login attempts, can you determine the secret numeric passcode?

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""

def main():
  key = []
  with open('p079/keylog.txt', 'r') as f:
    while True:
      line = f.readline()
      if not line:
        break
      prev = None
      for c in line.strip():
        c = int(c)
        if c not in key:
          if prev:
            # Place right of prev
            i = key.index(prev) + 1
            key.insert(i, c)
            pass
          else:
            key.insert(0, c)
        elif prev and key.index(c) < key.index(prev):
          # Move if not right of prev
          old = key.index(c)
          key.insert(key.index(prev) + 1, c)
          key.pop(old)
          pass
        prev = c
  print 'Key:', ''.join(str(c) for c in key)

if __name__ == '__main__':
  main()
