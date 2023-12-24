class Solution:
    def reverseVowels(self, s: str) -> str:
        res = [c for c in s]
        left, right = 0, len(s) - 1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                # both are vowels, swap
                res[left], res[right] = res[right], res[left]
                left += 1
                right -= 1

        return ''.join(res)
