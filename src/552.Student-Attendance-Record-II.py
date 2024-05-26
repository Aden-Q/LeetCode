class Solution:
    def checkRecord(self, n: int) -> int:
        # a typical dp problem
        mod = 10 ** 9 + 7

        # returns the number of possible attendance records of length n for
        # has_absence: true, if there's one absence record in the sequence
        # has_absence: false, if there's no absence record in the sequence
        # ending_with_L: whether the sequence ends with L
        @lru_cache
        def dp(n: int, has_absence: bool, ends_with_L: bool) -> int:
            if n == 0:
                return 0 if has_absence else 1

            if n == 1:
                if has_absence:
                    return 0 if ends_with_L else 1
                
                # 'L' or 'P'
                return 1
            
            if n == 2:
                if has_absence:
                    # 'AL', 'AP', 'LA', 'PA'
                    return 1 if ends_with_L else 3
                
                # 'LL', 'PP', 'LP', 'PL'
                return 2

            total = 0
            if has_absence:
                if not ends_with_L:
                    # if the current sequence ends with A, the previous sequence can either end with or w/o L
                    total += dp(n-1, False, True) + dp(n-1, False, False)
                    # if the current sequencee ends with P, the previous sequence must have A, and can either ends w/ or w/o L
                    total += dp(n-1, True, True) + dp(n-1, True, False)
                else:
                    # if the current sequence ends with L, the previous sequence must have A, and we need to make sure we don't have 3 consecutive L
                    total += dp(n-1, True, True) + dp(n-1, True, False) -  dp(n-3, True, False)
            else:
                if not ends_with_L:
                    # if the current sequence ends with P, the previous sequence must not have A, and can either ends w/ or w/o L
                    total += dp(n-1, False, True) + dp(n-1, False, False)
                else:
                    # if the current sequence ends with L, the previous sequence must not have A, and we need to make sure we don't have 3 consecutive L
                    total += dp(n-1, False, True) + dp(n-1, False, False) - dp(n-3, False, False)

            return total % mod

        s1 = dp(n, True, True)
        s2 = dp(n, True, False)
        s3 = dp(n, False, True)
        s4 = dp(n, False, False)

        return (s1 + s2 + s3 + s4) % mod
