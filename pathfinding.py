def find_path(src, target, passable):
    """
    >>> path = find_path((1, 1), (3, 4), lambda: True)
    >>> len(path)
    6
    >>> find_path((1, 1), (3, 1), lambda: True)
    [(1, 1), (2, 1), (3, 1)]

    :rtype: list or None if not found
    """
    paths = [[src]]
    visited = {src}
    # search until target is reached or all possible paths are discovered
    while len(paths) > 0:
        current_paths = paths
        paths = []
        for path in current_paths:
            for step in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                p = path[-1]
                dst = p[0] + step[0], p[1] + step[1]
                if passable(p, dst) and dst not in visited:
                    new_path = path.copy()
                    new_path.append(dst)
                    paths.append(new_path)
                    visited.add(dst)
                    if dst == target:
                        return new_path
    return None