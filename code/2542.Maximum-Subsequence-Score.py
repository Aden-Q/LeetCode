# a min heap
class Heap:
    def __init__(self, arr=[], k=None):
        self.heap = arr
        heapq.heapify(self.heap)
        self.sum = sum(arr)
        self.k = k

    def pushpop(self, val):
        heapq.heappush(self.heap, val)
        self.sum += val
        if len(self.heap) > self.k:
            self.sum -= heapq.heappop(self.heap)

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # sort decendingly based on nums2
        nums = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
        heap = Heap([x[0] for x in nums[:k-1]], k)
        max_sum = -math.inf

        for i in range(k-1, len(nums)):
            num1, num2 = nums[i][0], nums[i][1]
            heap.pushpop(num1)
            curr_sum = heap.sum * num2
            max_sum = max(max_sum, curr_sum)

        return max_sum