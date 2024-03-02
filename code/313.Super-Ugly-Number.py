class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        ptrs = [1] * len(primes)

        for i in range(2, n+1):
            dp[i] = min(dp[ptrs[j]] * primes[j] for j in range(len(primes)))
            for j in range(len(primes)):
                if dp[i] == dp[ptrs[j]] * primes[j]:
                    ptrs[j] += 1
            
        return dp[n]
