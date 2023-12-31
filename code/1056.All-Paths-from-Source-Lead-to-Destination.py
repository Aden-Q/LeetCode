class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for start, end in edges:
            if start == destination:
                return False
            adj[start].append(end)

        lead_to_destination = set()
        lead_to_destination.add(destination)
        def dfs(node, path) -> bool:
            nonlocal lead_to_destination
            # check whether there's a loop
            # violate the third condition: The number of possible paths from source to destination is a finite number.
            if node in path:
                return False

            if node in lead_to_destination:
                return True

            if len(adj[node]) == 0:
                return False

            path.append(node)
            for next_node in adj[node]:
                # if any of its neighbor does not lead to the destination, this node cannot lead to the destination
                if not dfs(next_node, path):
                    path.pop()
                    return False

            # if all of its neighbor leads to the destination, this node cannot lead to the destination
            path.pop()
            lead_to_destination.add(node)
            return True
            
        return dfs(source, [])