import sys

input_filename = sys.argv[1]


def elevate(input):
    step_count = 0
    item_count = 0
    for line in input.split('\n'):
        if item_count > 0:
            step_count += 2*item_count - 3
        item_count += line.count('generator')
        item_count += line.count('chip')
    return step_count

print(elevate(open(input_filename + '1').read()))
print(elevate(open(input_filename + '2').read()))
print(elevate(open(input_filename + '3').read()))
