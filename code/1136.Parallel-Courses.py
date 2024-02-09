class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # a typical typological sort problem
        adj = [[] for _ in range(n+1)]
        in_degrees = [0] * (n+1)
        queue = deque()
        for start, end in relations:
            adj[start].append(end)
            in_degrees[end] += 1
        
        for node in range(1, n+1):
            if in_degrees[node] == 0:
                queue.append(node)

        num_steps = 0
        courses_taken = 0
        while queue:
            num_steps += 1
            sz = len(queue)
            courses_taken += sz
            for _ in range(sz):
                curr_node = queue.popleft()
                # visit all its neighbors
                for next_node in adj[curr_node]:
                    in_degrees[next_node] -= 1
                    if in_degrees[next_node] == 0:
                        queue.append(next_node)
        
        return num_steps if courses_taken == n else -1
