class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for i in adj[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        return finish == numCourses

        