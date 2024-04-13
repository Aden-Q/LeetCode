class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            s, t = t, s

        if len(s) < len(t) - 1:
            return False

        # here we can safely assume len(s) <= len(t)
        if len(s) == len(t):
            idx = 0
            cnt_diff = 0
            while idx < len(s):
                if s[idx] != t[idx]:
                    cnt_diff += 1

                if cnt_diff > 1:
                    return False
                
                idx += 1
            
            # there must be exactly 1 diff
            return cnt_diff == 1

        # here we can safely assume len(s) = len(t) - 1, so we can only perform two operations: replace, delete
        idx = 0
        if s == '':
            return True

        while idx < len(s):
            if s[idx] != t[idx]:
                # we test two options
                # 1. replace
                # 2. delete (from t)
                return s[idx+1:] == t[idx+1:] or s[idx:] == t[idx+1:]
            
            idx += 1

        # s and t has the same prefix (s) and t has one more character
        return True
