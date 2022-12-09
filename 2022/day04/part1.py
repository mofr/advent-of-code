input = open('input').read()

fully_contain_count = 0
for pair_line in input.strip().split('\n'):
    r1, r2 = pair_line.split(',')
    r1 = tuple(map(int, r1.split('-')))
    r2 = tuple(map(int, r2.split('-')))
    if r1[0] >= r2[0] and r1[1] <= r2[1]:
        fully_contain_count += 1
    elif r1[0] <= r2[0] and r1[1] >= r2[1]:
        fully_contain_count += 1

print(fully_contain_count)
