class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0] + k

        min_heap = nums.copy()
        heapq.heapify(min_heap)
        while k:
            smallest = heapq.heappop(min_heap)
            second_smallest = min_heap[0]
            increment_val = min(k, max(1, second_smallest - smallest))
            smallest += increment_val
            heapq.heappush(min_heap, smallest)
            k -= increment_val

        prod = 1
        mod = 10 ** 9 + 7
        for num in min_heap:
            prod *= num
            prod = prod % (mod)

        return prod
