class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # a typical topological sort problem
        # graph node: character
        # graph edge: precedence relation
        n = len(words)
        adj = defaultdict(set)
        indegree = defaultdict(int)
        charset = set()
        edges = set()

        for c in words[0]:
            charset.add(c)

        for word in words:
            for c in word:
                charset.add(c)

        for i in range(1, n):
            curr_word = words[i]
            prev_word = words[i-1]

            idx = 0
            while idx < len(prev_word) or idx < len(curr_word):
                # if we find the first distinctive char, then we are done
                if idx < len(prev_word) and idx < len(curr_word) and prev_word[idx] != curr_word[idx]:
                    start, end = prev_word[idx], curr_word[idx]
                    adj[start].add(end)
                    edges.add((start, end))
                    break
                if idx == len(curr_word):
                    return ""
                idx += 1

        # now we can do topological sort
        indegree = defaultdict(int)
        for _, end in edges:
            indegree[end] += 1

        q = deque([])
        for c in charset:
            if indegree[c] == 0:
                q.append(c)

        ans = []
        while q:
            size = len(q)
            for _ in range(size):
                curr_node = q.popleft()
                ans.append(curr_node)
                for next_node in adj[curr_node]:
                    indegree[next_node] -= 1
                    if indegree[next_node] == 0:
                        q.append(next_node)

        return ''.join(ans) if len(ans) == len(charset) else ''