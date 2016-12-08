with open('day7_input') as f:
    input = f.read()


def support_tls(line):
    inside = False
    tls = False
    for i in range(len(line) - 3):
        if line[i] == '[':
            inside = True
        elif line[i] == ']':
            inside = False
        elif line[i] == line[i+3] and line[i+1] == line[i+2] and line[i] != line[i+1]:
            tls = not inside
            if inside:
                return tls
    return tls


def support_ssl(line):
    patterns = [set(), set()]
    inside = False
    for i in range(len(line) - 2):
        if line[i] == '[':
            inside = True
        elif line[i] == ']':
            inside = False
        elif line[i] == line[i+2] and line[i] != line[i+1]:
            patterns[inside].add((line[i], line[i+1]))
            if (line[i+1], line[i]) in patterns[not inside]:
                return True
    return False

tls_count = 0
ssl_count = 0
for line in input.split():
    if support_tls(line):
        tls_count += 1
    if support_ssl(line):
        ssl_count += 1

print(tls_count)
print(ssl_count)
