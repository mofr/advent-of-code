row = '.^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^'
row = list(map(lambda c: c == '^', row))
row_count = 400000


def next_row(row):
    result = [False] * len(row)
    row = [False] + row + [False]
    for i in range(len(row) - 2):
        result[i] = row[i] != row[i + 2]
    return result

count = 0
for _ in range(row_count):
    count += row.count(False)
    row = next_row(row)
print(count)
