class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
            indegree[edge[0]] += 1
        q = []
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
                
        # BFS
        path = []
        while len(q) != 0:
            node = q.pop()
            path.append(node)
            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        if len(path) == numCourses:
            return path
        return []