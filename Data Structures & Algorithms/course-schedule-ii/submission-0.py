class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)
        
        q = deque()
        result = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            val = q.popleft()
            result.append(val)
            for nei in adj[val]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return result if len(result) == numCourses else []
        