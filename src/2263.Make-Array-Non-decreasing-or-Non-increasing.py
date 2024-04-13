class Solution:
    def convertArray(self, nums: List[int]) -> int:
        def helper(nums) -> int:
            max_heap = []
            cost = 0
            for num in nums:
                if max_heap and -max_heap[0] > num:
                    cost += -heapq.heappop(max_heap) - num
                    heapq.heappush(max_heap, -num)
                heapq.heappush(max_heap, -num)

            return cost

        return min(helper(nums), helper(nums[::-1]))
