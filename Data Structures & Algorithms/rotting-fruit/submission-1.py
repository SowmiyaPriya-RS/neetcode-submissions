class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 2):
                    q.append((r,c))
                elif (grid[r][c] == 1):
                    fresh += 1

        if fresh == 0:
            return 0

        while q and fresh > 0:
            minutes += 1
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for i in range(len(q)):
                row, col = q.popleft()
                for r, c in directions:
                    dr, dc = row+r, col+c
                    if((dr < 0) or (dr == rows) or
                    (dc < 0) or (dc == cols) or
                    (grid[dr][dc] != 1)):
                        continue
                    q.append((dr, dc))
                    grid[dr][dc] = 2
                    fresh -= 1
        return minutes if fresh == 0 else -1
        