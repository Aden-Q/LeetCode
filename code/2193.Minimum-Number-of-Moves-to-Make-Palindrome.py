class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        left, right = 0, len(s) - 1
        total_moves = 0
        s = list(s)
        while left < right:
            if s[left] != s[right]:
                # greedy here
                first_end_char = left + 1
                while first_end_char < right and s[first_end_char] != s[right]:
                    first_end_char += 1

                first_start_char = right - 1
                while first_start_char > left and s[first_start_char] != s[left]:
                    first_start_char -= 1

                # compare
                if first_end_char - left <= right - first_start_char:
                    # perform left swap
                    total_moves += first_end_char - left
                    while first_end_char != left:
                        s[first_end_char], s[first_end_char-1] = s[first_end_char-1], s[first_end_char]
                        first_end_char -= 1
                else:
                    # perform right swap
                    total_moves += right - first_start_char
                    while first_start_char != right:
                        s[first_start_char], s[first_start_char+1] = s[first_start_char+1], s[first_start_char]
                        first_start_char += 1

            left += 1
            right -= 1

        return total_moves
