row = '.^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^'
row_count = 400000


def next_row(row):
    result = ''
    row = '.' + row + '.'
    for i in range(1, len(row) - 1):
        trap = row[i - 1] == row[i] != row[i + 1] or \
               row[i + 1] == row[i] != row[i - 1]
        result += '^' if trap else '.'
    return result

count = 0
for _ in range(row_count):
    count += row.count('.')
    row = next_row(row)

print(count)
