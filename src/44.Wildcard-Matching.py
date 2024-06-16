class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dp(s_idx: int, p_idx: int) -> bool:
            if len(s) == s_idx:
                for n_idx in range(p_idx, len(p)):
                    if p[n_idx] != "*":
                        return False

                return True

            if len(p) == p_idx:
                return False

            if p[p_idx] == "*":
                for next_idx in range(s_idx, len(s) + 1):
                    if dp(next_idx, p_idx + 1):
                        return True

            if p[p_idx] == "?":
                if s[s_idx:] == "":
                    return False

                # match exactly 1 character
                return dp(s_idx + 1, p_idx + 1)

            if p[p_idx] != s[s_idx]:
                return False

            return dp(s_idx + 1, p_idx + 1)

        return dp(0, 0)
