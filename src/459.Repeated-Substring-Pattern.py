class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for end in range(1, len(s) // 2 + 1):
            if len(s) % end != 0:
                continue
            sub_s = s[:end]
            start_idx = end
            while start_idx < len(s):
                if sub_s != s[start_idx:start_idx + end]:
                    break
                start_idx += end
            if start_idx >= len(s):
                return True
        return False