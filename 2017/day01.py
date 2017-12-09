import sys

input_filename = sys.argv[1]

with open(input_filename) as f:
    input = f.read()

result = 0
for i in range(len(input)):
    if input[i] == input[(i + len(input) // 2) % len(input)]:
        result += int(input[i])
        i += 1

print(result)
