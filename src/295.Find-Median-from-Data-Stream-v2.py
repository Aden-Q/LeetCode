class MedianFinder:

    def __init__(self):
        # we main one max heap (for the first half of input stream) and one min heap (for the second half of input stream)
        # by some order. And make sure the number of elements is balanced between the 2 heaps 
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        # we need to make sure we still maintain the ordering property
        top = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, top)
        # now if the min_heap is larger, we need to swap an element back
        if len(self.min_heap) > len(self.max_heap):
            top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -top) 

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        
        return -self.max_heap[0]
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()