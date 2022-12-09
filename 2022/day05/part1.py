input = open('input').read()

stacks_input, instructions = input.split('\n\n')
stacks_input_lines = stacks_input.split('\n')
stack_numbers = map(int, stacks_input_lines[-1].split())
stacks = []
for _ in stack_numbers:
    stacks.append([])
for line in stacks_input_lines[:-1]:
    for stack_index, i in enumerate(range(1, len(line), 4)):
        crate = line[i]
        if crate != ' ':
            stacks[stack_index].insert(0, crate)

for instruction in instructions.strip().split('\n'):
    _move, crate_count, _from, from_stack_index, _to, to_stack_index = instruction.split()
    crate_count = int(crate_count)
    from_stack_index = int(from_stack_index) - 1
    to_stack_index = int(to_stack_index) - 1
    crates = stacks[from_stack_index][-crate_count:]
    stacks[from_stack_index] = stacks[from_stack_index][:-crate_count]
    stacks[to_stack_index].extend(reversed(crates))

result = ''
for stack in stacks:
    result += stack[-1]

print(result)
