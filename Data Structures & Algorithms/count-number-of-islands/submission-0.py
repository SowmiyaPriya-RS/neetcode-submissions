class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols, = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            queue = collections.deque()
            visited.add((r, c))
            queue.append((r, c))

            while queue:
                r, c = queue.pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if(row in range(rows) and 
                       col in range(cols) and
                       grid[row][col] == "1" and 
                       (row, col) not in visited):
                       queue.append((row, col))
                       visited.add((row, col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands

        