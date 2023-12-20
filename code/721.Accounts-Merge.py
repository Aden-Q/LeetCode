class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # node of the graph: email
        graph = defaultdict(list)
        visited = defaultdict(bool)
        # build the graph
        for account in accounts:
            name = account[0]
            first_email = account[1]
            node = (name, first_email)
            visited[node] = False
            for email in account[2:]:
                next_node = (name, email)
                graph[node].append(next_node)
                graph[next_node].append(node)
                visited[next_node] = False
        
        def dfs(node, curr):
            if visited[node]:
                return
            
            visited[node] = True
            curr.append(node)
            for next_node in graph[node]:
                dfs(next_node, curr)
            
            return

        # dfs to get all connected components
        res = []
        for node in visited:
            if visited[node]:
                continue
            curr = []
            dfs(node, curr)
            # construct the result
            name = node[0]
            emails = sorted([x[1] for x in curr])
            res.append([name] + emails)

        return res
