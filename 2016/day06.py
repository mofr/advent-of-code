import sys

input_filename = sys.argv[1]

with open(input_filename) as f:
    input = f.read()


def most_common(lst):
    return max(set(lst), key=lst.count)


def least_common(lst):
    return min(set(lst), key=lst.count)

columns = []
for _ in range( len(input.split()[0])):
    columns.append([])

for line in input.split():
    for i, c in enumerate(line):
        columns[i].append(c)

print(''.join(map(least_common, columns)))
print(''.join(map(most_common, columns)))
