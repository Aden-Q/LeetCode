class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Vertex of the graph is alphabet chars
        # Edge of the graph is float numbers
        graph = defaultdict(defaultdict)
        for (divided, divisor), value in zip(equations, values):
            graph[divided][divisor] = value
            graph[divisor][divided] = 1 / value
        
        def dfs(cur, target, prod, visited):
            nonlocal graph
            visited.add(cur)
            res = -1
            if target in graph[cur]:
                # target found
                res = prod * graph[cur][target]
            else:
                # visit all its neighbours if not visited before
                for neighbor, value in graph[cur].items():
                    if neighbor in visited:
                        continue
                    res = dfs(neighbor, target, prod * value, visited)
                    if res != -1:
                        break
            visited.remove(cur)
            return res
        
        res = []
        # Evaluate for each query
        for divided, divisor in queries:
            if divided not in graph or divisor not in graph:
                res.append(-1)
            elif divided == divisor:
                res.append(1)
            else:
                # Search the graph
                visited = set()
                res.append(dfs(divided, divisor, 1, visited))
        
        return res