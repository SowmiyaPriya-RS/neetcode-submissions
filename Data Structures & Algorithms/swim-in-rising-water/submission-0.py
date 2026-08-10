class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [[grid[0][0], 0, 0]]
        visit = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        visit.add((0, 0))
        while heap:
            t, x, y = heapq.heappop(heap)
            if x == n-1 and y == n-1:
                return t
            for dr, dc in directions:
                row, col = dr+x, dc+y
                if row < 0 or col < 0 or row == n or col == n or (row, col) in visit:
                    continue
                visit.add((row, col))
                heapq.heappush(heap, [max(grid[row][col], t), row, col])


        