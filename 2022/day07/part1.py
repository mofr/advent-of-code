from collections import defaultdict

input = open('input').read()

current_dir = '/'
dir_stack = []
dirstat = defaultdict(int)

for line in input.split('\n'):
    if line.startswith('$ cd'):
        prompt, _cd, arg = line.split()
        if arg == '..':
            dir_stack.pop()
        elif arg == '/':
            dir_stack = []
        else:
            dir_stack.append(arg)
        current_dir = '/' + '/'.join(dir_stack)
    elif not line.startswith('$'):
        if not line.startswith('dir'):
            file_size, file_name = line.split()
            file_size = int(file_size)
            for i in range(len(dir_stack) + 1):
                abspath = '/' + '/'.join(dir_stack[:i])
                dirstat[abspath] += file_size

total = 0
for dirname, size in dirstat.items():
    if size <= 100000:
        total += size

print(total)
