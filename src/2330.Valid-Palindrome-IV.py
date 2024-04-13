class Solution:
    def makePalindrome(self, s: str) -> bool:
        
        # return true if we can make s[start:end] a palindrome using up to k operations
        @cache
        def dfs(start, end, k) -> bool:
            if k < 0:
                # invalid number of operations left
                return False
            if start == end:
                # if empty string, it's intrinsically a palindrome
                return True
            if end - start < k:
                # if the number of characters left is saller than k, we can change all of them to be the same character
                # which forms a palindrome
                return True

            # otherwise we compare s[start] and s[end-1]
            if s[start] == s[end-1]:
                return dfs(start+1, end-1, k)
            # otherwise we simply change the first character to be the same as the last character
            # and explore the remaining
            if dfs(start+1, end-1, k-1):
                return True

            return False

        return dfs(0, len(s), 2)