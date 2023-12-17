"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        # dfs returns a clone of the current node and make recursive calls to clone all its neighbors
        def dfs(currNode):
            if not currNode:
                return None
            if currNode in visited:
                return visited[currNode]
            
            # clone the current node
            visited[currNode] = Node(currNode.val)
            for neighbor in currNode.neighbors:
                # recursively copy all its neigbors
                visited[currNode].neighbors.append(dfs(neighbor))
            # once being out of the loop, visited[currNoded] is a complete copy of the original node,
            # with all neghbors attached
            return visited[currNode]

        return dfs(node)