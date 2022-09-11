import heapq

class Solution:
    # O(NlogN) time, log N for heapq push and pop, N for iteration
    # O(N) space
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [-float('inf')] * len(nums)
        dp[0] = nums[0]
        pq = []
        heapq.heappush(pq, [-dp[0], 0])
        
        for i in range(1, len(nums)):
            while pq[0][1] < i - k:
                heapq.heappop(pq)
            dp[i] = dp[pq[0][1]] + nums[i]
            heapq.heappush(pq, [-dp[i], i])
            
        return dp[-1]