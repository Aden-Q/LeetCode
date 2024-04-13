from heapq import heappush, heappop

class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        # O(nlogn)
        def feasible(k) -> list:
            # store elements from lower
            pq = []
            ans = []
            for num in nums:
                if pq and pq[0] + 2 * k == num:
                    ans.append(heappop(pq) + k)
                else:
                    heappush(pq, num)
            
            return ans if not pq else []

        k_candidates = set()
        # O(n)
        for i in range(1, len(nums)):
            k = (nums[i] - nums[0]) // 2
            if k > 0:
                k_candidates.add(k)

        for k in k_candidates:
            res = feasible(k)
            if res:
                return res
