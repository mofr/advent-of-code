def elevate(input):
    step_count = 0
    item_count = 0
    for line in input.split('\n'):
        if item_count > 0:
            step_count += (item_count - 2) * 2 + 1
        item_count += line.count('generator')
        item_count += line.count('chip')
    return step_count

print(elevate(open('day11_input1').read()))
print(elevate(open('day11_input2').read()))
