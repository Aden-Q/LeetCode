class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        path = [0]
        res = []
        
        def dfs(node):
            if node == n - 1:
                res.append(path[:])
                return
            
            for next_node in graph[node]:
                path.append(next_node)
                dfs(next_node)
                path.pop()
            
            return
        
        dfs(0)
        return res