import heapq

class MaxHeap:
    def __init__(self, val = []):
        self.heap = [-v for v in val]
        heapq.heapify(self.heap)
        self.size = len(val)
        
    def push(self, val):
        heapq.heappush(self.heap, -val)
        self.size += 1
        
    def pop(self):
        val = self.top()
        heapq.heappop(self.heap)
        self.size -= 1
        return val
        
    def top(self):
        return -self.heap[0]

    def getSize(self):
        return self.size
    
class MinHeap:
    def __init__(self, val = []):
        self.heap = [v for v in val]
        heapq.heapify(self.heap)
        self.size = len(val)
        
    def push(self, val):
        heapq.heappush(self.heap, val)
        self.size += 1
        
    def pop(self):
        val = self.top()
        heapq.heappop(self.heap)
        self.size -= 1
        return val
    
    def top(self):
        return self.heap[0]
        
    def getSize(self):
        return self.size

class MedianFinder:
    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()

    def addNum(self, num: int) -> None:
        size1 = self.min_heap.getSize()
        size2 = self.max_heap.getSize()
        if size1 == 0 and size2 == 0:
            self.min_heap.push(num)
            return
        elif size2 == 0:
            if num > self.min_heap.top():
                self.min_heap.push(num)
                self.max_heap.push(self.min_heap.pop())
            else:
                self.max_heap.push(num)
            return
            
        if num >= self.min_heap.top():
            self.min_heap.push(num)
            if size1 > size2:
                self.max_heap.push(self.min_heap.pop())
        else:
            self.max_heap.push(num)
            if size2 > size1:
                self.min_heap.push(self.max_heap.pop())       

    def findMedian(self) -> float:
        size1 = self.min_heap.getSize()
        size2 = self.max_heap.getSize()
        if size1 < size2:
            return self.max_heap.top()
        elif size1 > size2:
            return self.min_heap.top()
        return (self.min_heap.top() + self.max_heap.top()) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()