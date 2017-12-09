import hashlib
import sys

input_filename = sys.argv[1]

with open(input_filename) as f:
    input = f.read()

common_hash = hashlib.md5()
common_hash.update(input.encode())
i = 0
password = ['_'] * 8
while True:
    hash = common_hash.copy()
    hash.update(str(i).encode())
    md5 = hash.hexdigest()
    if md5.startswith('00000'):
        pos = int(md5[5], 16)
        if pos < len(password) and password[pos] == '_':
            password[pos] = md5[6]
            if '_' not in password:
                break

    i += 1

print(''.join(password))