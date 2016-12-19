import hashlib
from functools import lru_cache


def triple(hex, c):
    for x in range(32 - 2):
        if hex[x] == hex[x+1] == hex[x+2]:
            return hex[x] == c
    return False


def fives(hex):
    x = 0
    while x <= 32 - 5:
        if hex[x] == hex[x+1] == hex[x+2] == hex[x+3] == hex[x+4]:
            yield hex[x]
            x += 4
        x += 1


@lru_cache(maxsize=1024)
def hash(index):
    global salt
    md5 = hashlib.md5()
    md5.update(salt+str(index).encode())
    for _ in range(2016):
        prev = md5.hexdigest().encode()
        md5 = hashlib.md5()
        md5.update(prev)
    return md5.hexdigest()

salt = b'jlmsuwbz'

i = 0
keys = set()
while len(keys) < 64:
    for c in fives(hash(i)):
        for offset in range(1000, 0, -1):
            if i - offset < 0:
                continue
            if triple(hash(i - offset), c):
                keys.add(i - offset)

    i += 1

keys = sorted(list(keys))

print(keys[63])
