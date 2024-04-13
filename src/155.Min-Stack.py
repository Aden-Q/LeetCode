class MinStack:

    def __init__(self):
        self.stack = []
        self.running_min = math.inf

    def push(self, val: int) -> None:
        curr_min = min(val, self.running_min)
        self.running_min = min(self.running_min, curr_min)
        self.stack.append((val, curr_min))

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) == 0:
            self.running_min = math.inf
        else:
            self.running_min = self.stack[-1][1]
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.running_min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()