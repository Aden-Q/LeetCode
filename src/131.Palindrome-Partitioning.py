class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(s) -> bool:
            return s == s[::-1]

        def dfs(s, path):
            nonlocal result
            
            if not s:
                result.append(path)
            
            for i in range(1, len(s) + 1):
                if isPalindrome(s[:i]):
                    dfs(s[i:], path + [s[:i]])
        
        
        dfs(s, [])
        return result
