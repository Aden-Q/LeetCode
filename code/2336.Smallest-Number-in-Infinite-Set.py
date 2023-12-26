class SmallestInfiniteSet:
    def __init__(self):
        # the min_heap is used to keep track of all discrete elements that are < start_of_stream
        self.min_heap = []
        # heap_members is used to quikly check whether some member is in the heap
        self.heap_members = set()
        # this is the minimum number of a continuous infinite stream
        # the idea behind is that we can only pop from the left (smallest element) of the stream
        # while always preserving the continuity proterty of the stream
        # we only need to keep track of the start of this stream
        # the trick is that we will only consume this stream, never produce new elements into it (we can but it's a little complex)
        self.start_of_stream = 1

    def popSmallest(self) -> int:
        if self.min_heap:
            number_to_remove = heapq.heappop(self.min_heap)
            self.heap_members.remove(number_to_remove)
            return number_to_remove
        # otherwise we need to pop from the stream
        self.start_of_stream += 1
        return self.start_of_stream - 1

    def addBack(self, num: int) -> None:
        if num >= self.start_of_stream:
            return
        if num in self.heap_members:
            return
        self.heap_members.add(num)
        heapq.heappush(self.min_heap, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)