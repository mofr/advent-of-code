class Elf:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self.next

    def __repr__(self):
        return str(self.value)

n = 3001330
elfs = list(map(Elf, range(1, n + 1)))
for i, elf in enumerate(elfs):
    elf.next = elfs[(i + 1) % n]
    elf.prev = elfs[(i - 1) % n]

e = elfs[n // 2]
if n % 2 == 0:
    e = e.remove()

while e != e.next:
    e = e.remove()
    e = e.next
    e = e.remove()

print(e)
