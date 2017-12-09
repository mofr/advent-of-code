import sys

input_filename = sys.argv[1]

with open(input_filename) as f:
    input = f.read()

possible_triangles = 0
for line in input.strip().split('\n'):
    sides = map(int, line.strip().split())
    sides = sorted(sides)
    can_be_triangle = sides[0] + sides[1] > sides[2]
    if can_be_triangle:
        possible_triangles += 1

print(possible_triangles)


def group(iterator, count):
    itr = iter(iterator)
    while True:
        yield [next(itr) for _ in range(count)]

numbers = list(map(int, input.strip().split()))
numbers = numbers[::3] + numbers[1::3] + numbers[2::3]
possible_triangles_vertically = 0
for sides in group(numbers, 3):
    sides = sorted(sides)
    can_be_triangle = sides[0] + sides[1] > sides[2]
    if can_be_triangle:
        possible_triangles_vertically += 1

print(possible_triangles_vertically)
