class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        adj = [[] for i in range(n)]
        visit = set()

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)

        for i in range(n):
            if i not in visit:
                count += 1
                dfs(i)

        return count
        