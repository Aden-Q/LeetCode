class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
        on_path = [False] * numCourses
        visited = [False] * numCourses
        res = []
        has_cycle = False
        
        def traverse(node):
            nonlocal graph, on_path, visited, res, has_cycle
            if on_path[node]:
                has_cycle = True
            if has_cycle or visited[node]:
                return
            # visit the current node
            visited[node] = True
            on_path[node] = True
            # vist all neighbours
            for neighbour in graph[node]:
                traverse(neighbour)
            res.append(node)
            on_path[node] = False
            return
        
        for node in range(numCourses):
            traverse(node)
            
        if has_cycle:
            return []
        
        res.reverse()
        return res