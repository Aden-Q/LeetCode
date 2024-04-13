class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [n-1]

        neighbors = [set() for _ in range(n)]
        # build the adjacency list graph
        for edge in edges:
            first, second = edge
            neighbors[first].add(second)
            neighbors[second].add(first)

        leaves = [i for i in range(n) if len(neighbors[i]) == 1]
        while n > 2:
            size = len(leaves)
            n -= size
            new_leaves = []
            for leave in leaves:
                neighbor = neighbors[leave].pop()
                neighbors[neighbor].remove(leave)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            leaves = new_leaves
        
        return leaves