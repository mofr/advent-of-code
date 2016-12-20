with open('day20_input') as f:
    input = f.read()


class Firewall:
    def __init__(self):
        self.ranges = []

    def add(self, lo, hi):
        for i, (i_lo, i_hi) in enumerate(self.ranges):
            if lo <= i_hi + 1 and hi >= i_lo - 1:
                lo = min(lo, i_lo)
                hi = max(hi, i_hi)
                del self.ranges[i]
                self.add(lo, hi)
                return

        self.ranges.append((lo, hi))

    def count(self):
        return sum([hi - lo + 1 for lo, hi in self.ranges])

firewall = Firewall()

for line in input.split():
    lo, hi = map(int, line.split('-'))
    firewall.add(lo, hi)

firewall.ranges = sorted(firewall.ranges)
print(firewall.ranges[0][1] + 1)
print((1 << 32) - firewall.count())
