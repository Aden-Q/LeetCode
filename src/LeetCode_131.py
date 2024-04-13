class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s:str):
            if s == s[::-1]:
                return True
            else:
                return False
        path = []
        res = []
        size = len(s)
        def backtracking(s, start):
            nonlocal path, res, size
            if start > size - 1 and path:
                res.append(path[:])
                return
            for i in range(start, size):
                if is_palindrome(s[start:i+1]):
                    path.append(s[start:i+1])
                    backtracking(s, i+1)
                    path.pop()
        backtracking(s, 0)
        if size == 0:
            return []
        else:
            return res