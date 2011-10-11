"""
Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange). For
example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and without
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method
is to use a password as a key. If the password is shorter than the message,
which is likely, the key is repeated cyclically throughout the message. The
balance for this method is using a sufficiently long password key for security,
but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case
characters. Using cipher1.txt (right click and 'Save Link/Target As...'), a file
containing the encrypted ASCII codes, and the knowledge that the plain text must
contain common English words, decrypt the message and find the sum of the ASCII
values in the original text.
"""

import os

def encrypt(text, key):
    encrypted = []
    key_n = 0
    for char in text:
        key_c = ord(key[key_n])
        encrypted.append(ord(char) ^ key_c)
        key_n += 1
        if key_n >= len(key):
            key_n = 0
    return encrypted
def decrypt(encrypted, key):
    decrypted = []
    key_n = 0
    for char in encrypted:
        key_c = ord(key[key_n])
        decrypted.append(chr(char ^ key_c))
        key_n += 1
        if key_n >= len(key):
            key_n = 0
    return ''.join(decrypted)

def get_key(encrypted, key_len=3):
    keys = []
    chars = []
    valid_chars = range(ord('a'), ord('z') + 1)
    for i in range(key_len):
        chars.append(list(valid_chars))
    # Loop through the encrypted text, clearing out invalid key chars
    key_n = 0
    for value in encrypted:
        for c in chars[key_n]:
            result = value ^ c
            #if result not in valid_results:
            if result < 0x20 or result > 0x7e:
                chars[key_n].remove(c)
        key_n += 1
        if key_n >= key_len:
            key_n = 0
    #print chars
    # gather keys
    keys = [chr(c) for c in chars[0]]
    for n in range(1, key_len):
        _keys = []
        for last in keys:
            for c in chars[n]:
                _keys.append(last + chr(c))
        keys = _keys
    words = ['there', 'who', 'the', 'is', 'in', 'it']
    scored = []
    for k in keys:
        d = decrypt(encrypted, k)
        score = 1
        for word in words:
            if word in d:
                score *= len(word)
        scored.append((score, k))
    return sorted([s for s in scored if s[0] > 1])
    

def main():
    #e = encrypt('Myles is a ridiculous dog who loves his bone', 'amz')
    #print get_key(e)
    with open(os.path.join(os.path.dirname(__file__), 'p059', 'cipher1.txt'), 'r') as codefile:
        codes = [int(c) for c in codefile.readline().split(',')]
    best = get_key(codes)[-1][1]
    print 'Using', best
    d = decrypt(codes, best)
    print 'Decrypted:'
    print d
    print 'Sum:', sum([ord(c) for c in d])

if __name__ == '__main__':
    main()
