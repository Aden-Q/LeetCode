class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # we can maintain a max heap of size k, the top of the heap is the kth largest element
        # we've seen so far
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]