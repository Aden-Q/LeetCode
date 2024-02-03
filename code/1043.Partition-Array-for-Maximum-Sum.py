class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        # returns the max sum we can get starting from arr[start] following the rules
        @cache
        def dp(start) -> int:
            nonlocal k
            if start >= len(arr):
                # there's no more elements in arr to partition
                return 0
            
            # perform a local partition
            currMax = arr[start]
            res = 0
            for end in range(start, min(start+k, len(arr))):
                currMax = max(currMax, arr[end])
                res = max(res, (end - start + 1) * currMax + dp(end+1))
            
            return res
        
        return dp(0)
