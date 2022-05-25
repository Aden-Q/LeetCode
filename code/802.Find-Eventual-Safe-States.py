class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # 0: not visited
        # 1: visited before
        # 2: safe node, should be returned
        state = [0] * n
        
        def safe(node):
            if state[node] > 0:
                return state[node] == 2
            state[node] = 1
            for next_node in graph[node]:
                if not safe(next_node):
                    return False
            state[node] = 2
            return True
        
        return [i for i in range(n) if safe(i)]