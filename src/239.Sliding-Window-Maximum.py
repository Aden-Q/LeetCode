from collections import deque
class MyQueue:
    def __init__(self):
        self.queue = deque()
    
    def pop(self, value):
        if self.queue[0] != value:
            return
        else:
            self.queue.popleft()
        
    def push(self, value):
        while self.queue and self.queue[-1] < value:
            self.queue.pop()
        self.queue.append(value)
        
    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = MyQueue()
        if len(nums) < k:
            return [max(nums)]
        res = []
        for i in range(k):
            queue.push(nums[i])
        res.append(queue.front())
        for i in range(k, len(nums)):
            queue.pop(nums[i-k])
            queue.push(nums[i])
            res.append(queue.front())
            
        return res