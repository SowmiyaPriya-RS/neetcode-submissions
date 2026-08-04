class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        minheap = [(0, k)]
        t = 0
        visited = set()

        for u, v, w in times:
            adj[u].append((v, w))

        while(minheap):
            t1, v1 = heapq.heappop(minheap)
            if v1 in visited:
                continue
            visited.add(v1)
            t = t1

            for v2, t2 in adj[v1]:
                if v2 not in visited:
                    heapq.heappush(minheap, (t1+t2, v2))

        return t if len(visited) == n else -1

        