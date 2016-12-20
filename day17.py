import hashlib

input = b'bwnlcvfs'


def hash(data):
    md5 = hashlib.md5()
    md5.update(data)
    return map(lambda x: x >= 'b', md5.hexdigest()[:4])


class Path:
    def __init__(self, path=b'', x=0, y=0):
        self.path = path
        self.x = x
        self.y = y

    def split(self):
        u, d, l, r = hash(input + self.path)
        if u and self.y > 0:
            yield Path(self.path + b'U', self.x, self.y - 1)
        if d and self.y < 3:
            yield Path(self.path + b'D', self.x, self.y + 1)
        if l and self.x > 0:
            yield Path(self.path + b'L', self.x - 1, self.y)
        if r and self.x < 3:
            yield Path(self.path + b'R', self.x + 1, self.y)

    def __repr__(self):
        return self.path.decode()


def find():
    paths = [Path()]

    while len(paths):
        next_paths = []
        for p in paths:
            if p.x == 3 and p.y == 3:
                yield p
            else:
                next_paths.extend(p.split())
        paths = next_paths

paths = list(find())
paths = sorted(paths, key=lambda p: len(p.path))
print(paths[0])
print(len(paths[-1].path))
