class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # then we must delete either left or right
                delete_left = s[:left] + s[left+1:]
                if delete_left == delete_left[::-1]:
                    return True
                delete_right = s[:right] + s[right+1:]
                return delete_right == delete_right[::-1]
            left += 1
            right -= 1
        
        return True
