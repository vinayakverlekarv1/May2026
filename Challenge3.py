def count_clusters(grid: list[list[int]]) -> int:
    """
    DFS flood-fill to count connected clusters of 1s.
    Connectivity: 4-directional (up/down/left/right).
    """
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if visited[r][c] or grid[r][c] == 0:
            return
        visited[r][c] = True
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            dfs(r + dr, c + dc)

    clusters = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                clusters += 1

    return clusters


# --- Input ---
flat = [1,1,0,0,1, 0,1,1,0,0, 0,0,1,0,1, 1,0,0,1,1, 0,0,1,0,0]
grid = [flat[i*5:(i+1)*5] for i in range(5)]

print(count_clusters(grid))  # Output: 5