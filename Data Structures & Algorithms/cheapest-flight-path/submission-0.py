class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        adj = [[] for i in range(n)]

        for s, d, cost in flights:
            adj[s].append([d, cost])

        q = deque([(0, src, 0)])
        while q:
            cost, node, stops = q.popleft()
            if stops > k:
                continue
            for nei, c in adj[node]:
                newcost = cost + c
                if newcost < prices[nei]:
                    prices[nei] = newcost
                    q.append((newcost, nei, stops+1))
        return prices[dst] if prices[dst] != float("inf") else -1
    
            

        