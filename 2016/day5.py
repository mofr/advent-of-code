import hashlib
import time

with open('day5_input') as f:
    input = f.read()

common_hash = hashlib.md5()
common_hash.update(input.encode())
start = time.clock()
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
            print(''.join(password))
            if '_' not in password:
                break

    i += 1

print('Elapsed {} s'.format(time.clock() - start))
print('i = {}'.format(i))
