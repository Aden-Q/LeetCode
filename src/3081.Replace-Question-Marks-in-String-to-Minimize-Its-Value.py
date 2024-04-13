class Solution:
    def minimizeStringValue(self, s: str) -> str:
        s_transform = ['?'] * len(s)
        table = Counter()
        for c in 'abcdefghijklmnopqrstuvwxyz':
            table[c] = 0
            
        for c in s:
            if c != '?':
                table[c] += 1
            
        indices = []
        for i, c in enumerate(s):
            if c == '?':
                candidates = [(val, key) for key, val in table.items()]
                candidates.sort(key = lambda x: (x[0], x[1]))
                indices.append(candidates[0][1])
                table[candidates[0][1]] += 1
                
        indices.sort()
        indices = deque(indices)
        for i in range(len(s)):
            if s[i] != '?':
                s_transform[i] = s[i]
            else:
                s_transform[i] = indices.popleft()
        
        return ''.join(s_transform)
