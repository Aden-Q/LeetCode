class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = []
        res = []
        
        def traverse(cur, target):
            nonlocal graph
            path.append(cur)
            if cur == target:
                res.append(path[:])
                path.pop()
                return
            for node in graph[cur]:
                traverse(node, target)
            path.pop()
            return
            
        traverse(0, len(graph) - 1)
        return res