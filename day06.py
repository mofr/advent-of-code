def most_common(lst):
    return max(set(lst), key=lst.count)


def least_common(lst):
    return min(set(lst), key=lst.count)

with open('day06_input') as f:
    input = f.read()

columns = []
for _ in range( len(input.split()[0])):
    columns.append([])

for line in input.split():
    for i, c in enumerate(line):
        columns[i].append(c)

print(''.join(map(least_common, columns)))
print(''.join(map(most_common, columns)))
