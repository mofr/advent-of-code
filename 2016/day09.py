import sys

input_filename = sys.argv[1]

with open(input_filename) as f:
    input = f.read()

input = input.replace(' ', '')


def decompress(data):
    start = None
    result = 0
    i = 0
    while i < len(data):
        if data[i] == '(':
            start = i+1
        elif data[i] == ')':
            num, repeat = map(int, data[start:i].split('x'))
            i += 1
            result += decompress(data[i:i+num]) * repeat
            i += num - 1
            start = None
        elif start is None:
            result += 1
        i += 1
    return result

output = decompress(input)

print(output)
