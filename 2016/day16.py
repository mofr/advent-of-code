state = '10011111011011001'
disk_length = 35651584

def mutate(a):
    b = ''.join(['1' if x == '0' else '0' for x in reversed(a)])
    return a + '0' + b


def checksum(a):
    result = ''
    i = 0
    while i < len(a) - 1:
        if a[i] == a[i+1]:
            result += '1'
        else:
            result += '0'
        i += 2
    if len(result) % 2 != 1:
        result = checksum(result)
    return result


while len(state) < disk_length:
    state = mutate(state)
state = state[:disk_length]
print(checksum(state))
