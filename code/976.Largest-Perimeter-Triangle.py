import heapq

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums_temp = [-num for num in nums]
        heapq.heapify(nums_temp)
        a = -heapq.heappop(nums_temp)
        b = -heapq.heappop(nums_temp)
        c = -heapq.heappop(nums_temp)
        if b + c > a:
            return a + b + c
        while len(nums_temp) > 0:
            a, b, c = b, c, -heapq.heappop(nums_temp)
            if b + c > a:
                return a + b + c
        return 0