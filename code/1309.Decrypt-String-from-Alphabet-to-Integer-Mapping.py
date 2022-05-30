class Solution:
    def freqAlphabets(self, s: str) -> str:
        map_table = {}
        for c in 'abcdefghi':
            map_table[str(ord(c) - ord('a') + 1)] = c
        for c in 'jklmnopqrstuvwxyz':
            map_table[str(ord(c) - ord('j') + 10) + '#'] = c
        res = []
        p = 0
        while p < len(s):
            if p + 2 < len(s) and s[p+2] == '#':
                res.append(map_table[s[p:p+3]])
                p += 3
            else:
                res.append(map_table[s[p]])
                p += 1
        return ''.join(res)