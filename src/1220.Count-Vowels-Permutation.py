class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        # counting dp
        # we are going to build a string of length n
        # the current character is affected by the following characters
        # idx: the current idx of the string we are considering
        # prev_char: the previous character used to build the string
        # returns the number of ways to build a string with all the constraints ending at some idx
        # iterate from left to right so that we know the previous character to build the current one
        @cache
        def dp(idx: int, prev_char: str) -> int:
            if idx == n:
                return 1

            ans = 0
            if prev_char == 'a':
                ans += dp(idx+1, 'e') % mod
                return ans
            if prev_char == 'e':
                for c in 'ai':
                    ans = (ans + dp(idx+1, c)) % mod
                return ans
            if prev_char == 'i':
                for c in 'aeou':
                    ans = (ans + dp(idx+1, c)) % mod
                return ans
            if prev_char == 'o':
                for c in 'iu':
                    ans = (ans + dp(idx+1, c)) % mod
                return ans
            if prev_char == 'u':
                for c in 'a':
                    ans = (ans + dp(idx+1, c)) % mod
                return ans
            else:
                # initial case
                for c in 'aeiou':
                    ans = (ans + dp(idx+1, c)) % mod
                return ans

        # we want to start building from index 0 and the previous used character is empty, indicating nothing used before
        # so we can choose any character to be the first one
        return dp(0, '')