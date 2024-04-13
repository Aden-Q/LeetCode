class Solution:
    def countVowelStrings(self, n: int) -> int:
        d = ['a', 'e', 'i', 'o', 'u']
        path = []
        count = 0
        
        def backtracking(n, start):
            nonlocal count
            if n == 0:
                count += 1
                return
            for i in range(start, 5):
                path.append(d[i])
                backtracking(n-1, i)
                path.pop()
            return
        
        backtracking(n, 0)
        return count