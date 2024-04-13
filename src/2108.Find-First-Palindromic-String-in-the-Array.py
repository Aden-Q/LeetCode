class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def isPalindromic(s: str) -> bool:
            first, second = 0, len(s) - 1
            while first < second:
                if s[first] != s[second]:
                    return False
                first += 1
                second -= 1

            return True

        for word in words:
            if isPalindromic(word):
                return word

        return ""
