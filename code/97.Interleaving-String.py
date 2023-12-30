class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        # end1: end of s1, exclusive
        # end2: end of s2, exclusive
        # return whether we can interleave s1[:end1] and s2[:end2] to form s3[:end1+end2]
        @cache
        def dp(end1: int, end2: int) -> bool:
            if end1 == 0:
                return s3[:end2] == s2[:end2]
            if end2 == 0:
                return s3[:end1] == s1[:end1]

            if s1[end1-1] == s3[end1+end2-1]:
                if dp(end1-1, end2):
                    return True
            if s2[end2-1] == s3[end1+end2-1]:
                return dp(end1, end2-1)

        return dp(m, n)
