class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        total = 0
        prev_end = 0
        for ss in s:
            if ss == c:
                prev_end = prev_end + 1
                total += prev_end
                
        return total
