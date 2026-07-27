class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(i, j):
            q = collections.deque()
            visited.add((i, j))
            q.append((i, j))
            length = 1

            while q:
                r, c = q.pop()
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dr, dc in directions:
                    row, col = dr+r, dc+c
                    if (row in range(rows) and 
                       col in range(cols) and
                       grid[row][col] == 1 and 
                       (row, col) not in visited):
                        visited.add((row, col))
                        q.append((row, col))
                        length += 1
            return length


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, bfs(i, j))
        return max_area
                    


        