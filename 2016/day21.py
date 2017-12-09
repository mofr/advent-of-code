import sys

input_filename = sys.argv[1]

with open(input_filename) as f:
    input = f.read()

password = list('fbgdceah')


def rotate(l, n):
    n %= len(l)
    return l[-n:] + l[:-n]


for line in reversed(input.split('\n')):
    if line.startswith('rotate left'):
        offset = int(line.split()[2])
        password = rotate(password, offset)
    elif line.startswith('rotate right'):
        offset = int(line.split()[2])
        password = rotate(password, -offset)
    elif line.startswith('rotate based'):
        letter = line.split()[-1]
        shift = 1

        while True:
            index = rotate(password, -shift).index(letter)
            if shift == index + 1 + (index >= 4):
                break
            shift += 1

        password = rotate(password, -shift)
    elif line.startswith('move'):
        p1 = int(line.split()[2])
        p2 = int(line.split()[-1])
        p1, p2 = p2, p1
        letter = password[p1]
        del password[p1]
        password.insert(p2, letter)
    elif line.startswith('reverse'):
        p1 = int(line.split()[2])
        p2 = int(line.split()[-1])
        password = password[:p1] + list(reversed(password[p1:p2+1])) + password[p2+1:]
    elif line.startswith('swap position'):
        p1 = int(line.split()[2])
        p2 = int(line.split()[-1])
        letter1 = password[p1]
        letter2 = password[p2]
        password[p1] = letter2
        password[p2] = letter1
    elif line.startswith('swap letter'):
        letter1 = line.split()[2]
        letter2 = line.split()[-1]
        index1 = password.index(letter1)
        index2 = password.index(letter2)
        password[index1] = letter2
        password[index2] = letter1

print(''.join(password))
