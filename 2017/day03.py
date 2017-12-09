input = '361527'
input = int(input)


def walk():
    number = 1
    sign = 1
    while True:
        for _ in range(number):
            yield sign, 0
        for _ in range(number):
            yield 0, sign
        number += 1
        sign = -sign


def calc_position(index):
    pos = (0, 0)
    for i, (dx, dy) in enumerate(walk()):
        pos = (pos[0] + dx, pos[1] + dy)
        if i + 2 == index:
            return pos


pos = calc_position(input)
distance = abs(pos[0]) + abs(pos[1])
print(distance)

values = [1]
indexes = {(0, 0): 0}
pos = (0, 0)
for i, (dx, dy) in enumerate(walk()):
    pos = (pos[0] + dx, pos[1] + dy)
    i = i + 1
    indexes[pos] = i

    i1 = indexes.get((pos[0] - 1, pos[1] - 1))
    i2 = indexes.get((pos[0] - 1, pos[1] + 1))
    i3 = indexes.get((pos[0] - 1, pos[1]))
    i4 = indexes.get((pos[0] + 1, pos[1] - 1))
    i5 = indexes.get((pos[0] + 1, pos[1] + 1))
    i6 = indexes.get((pos[0] + 1, pos[1]))
    i7 = indexes.get((pos[0], pos[1] + 1))
    i8 = indexes.get((pos[0], pos[1] - 1))
    value = 0
    value += values[i1] if i1 is not None else 0
    value += values[i2] if i2 is not None else 0
    value += values[i3] if i3 is not None else 0
    value += values[i4] if i4 is not None else 0
    value += values[i5] if i5 is not None else 0
    value += values[i6] if i6 is not None else 0
    value += values[i7] if i7 is not None else 0
    value += values[i8] if i8 is not None else 0

    if value > input:
        print(value)
        break

    values.append(value)
