import re

with open('day4_input') as f:
    input = f.read()


def check(name, checksum):
    name = name.replace('-', '')
    score = {}
    for c in name:
        score[c] = score.get(c, 0) + 1

    for i in range(len(checksum) - 1):
        c1, c2 = checksum[i], checksum[i+1]
        s1, s2 = score.get(c1, 0), score.get(c2, 0)
        if s1 == 0 or s2 == 0:
            return False
        if s1 == s2 and c1 > c2:
            return False
        if s1 < s2:
            return False

    return True


def decrypt(name, count):
    result = ''
    max_range = ord('z') - ord('a') + 1
    for c in name:
        if c == '-':
            result += ' '
        else:
            result += chr((ord(c) - ord('a') + count) % max_range + ord('a'))
    return result

id_sum = 0
rooms = []
for line in input.split():
    name, id, checksum = re.match('(.*?)-(\\d+)\\[(.+)\\]', line).groups()
    id = int(id)
    real_room = check(name, checksum)
    if real_room:
        id_sum += id
        rooms.append((name, id))

print(id_sum)

for name, id in rooms:
    name = decrypt(name, id)
    if 'north' in name:
        print(id, name)
