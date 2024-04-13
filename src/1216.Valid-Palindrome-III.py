class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        # returns True if the substring s[start:end] can be transformed into a palindrome
        # if we can remove at most k characters from it
        @cache
        def dfs(start, end, k):
            if k < 0:
                return False
            if end - start <= k:
                # if the number of characters left is <= k, we can remove them all to form a palindrome
                return True
            
            # otherwise we run dfs to search for solutions
            if s[start] == s[end-1]:
                # in a greedy manner, we shouldn't do anything
                return dfs(start+1, end-1, k)
            
            # check if we can remove the first character to get a palindrome
            if dfs(start+1, end, k-1):
                return True
            # if failed, we further check if we can remove the last character to get a palindrome
            if dfs(start, end-1, k-1):
                return True

            # if both failed, no way to get a palindrome
            return False

        return dfs(0, len(s), k)