from collections import deque

def is_valid(s: str) -> bool:
    """No 'CC' substring. Only A, B, C chars."""
    return 'CC' not in s and all(c in 'ABC' for c in s)

def get_neighbours(s: str) -> list[str]:
    """All valid single-character mutations."""
    neighbours = []
    for i, ch in enumerate(s):
        for replacement in 'ABC':
            if replacement != ch:
                candidate = s[:i] + replacement + s[i+1:]
                if is_valid(candidate):
                    neighbours.append(candidate)
    return neighbours

def bfs_shortest_paths(start: str, end: str) -> tuple[int, int]:
    """
    BFS tracking:
    - dist: shortest distance to each node
    - path_count: number of shortest paths to each node
    """
    if start == end:
        return 0, 1

    dist       = {start: 0}
    path_count = {start: 1}
    queue      = deque([start])

    while queue:
        current = queue.popleft()
        current_dist = dist[current]

        # Once we've settled the target, stop expanding further
        if current == end:
            break

        for neighbour in get_neighbours(current):
            if neighbour not in dist:
                # First time reaching this node
                dist[neighbour]       = current_dist + 1
                path_count[neighbour] = path_count[current]
                queue.append(neighbour)

            elif dist[neighbour] == current_dist + 1:
                # Another shortest path arrives at same node
                path_count[neighbour] += path_count[current]

    if end not in dist:
        return -1, 0

    return dist[end], path_count[end]


length, paths = bfs_shortest_paths("CBAB", "ABCB")
print(f"Length: {length}")
print(f"Paths:  {paths}")