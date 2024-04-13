class BrowserHistory:
    # First, considering the requirement to go forward && backward
    # There are two useful data structure: array or doulby-linked list
    # The trade off is between visit and back/forward
    # Array allows us quick forward and backward, but slow visit (in the sense that we need to clear the forward history)
    # Doulby linked list allows really fast visit, but slow forward and backward (because we can only move one step at a time)
    # Besides, doubly linked list allows dynamic memory allocation thus better scalability, while array has the drawback of limited capacity
    # Because the memory allocated for array has to be continuous in memory
    # Theoretically this is an efficiently system supporting O(1) time for all operations
    # The only concern is for increasing the history capacity, which rarely happens, so can be ignored, thus amortized O(1) for all operations
    
    def __init__(self, homepage: str):
        self.history = [homepage] + [0] * 999
        self.size = 1 # The size of the current browser history
        self.capacity = 1000  # The maximum capacity of the browser history
        self.ptr = 0

    def visit(self, url: str) -> None:
        if self.ptr == self.capacity - 1:
            # Enlarge the capacity by a factor of 2 each time
            self.history += [None] * capacity
            self.capacity *= 2
            self.ptr += 1
            self.size += 1
            self.history[ptr] = url
        else:
            # Otherwise we have enough capacity
            self.ptr += 1
            self.history[self.ptr] = url
            # This is a lazy delete by marking those entries coming later as unusable
            self.size = self.ptr + 1

    def back(self, steps: int) -> str:
        self.ptr -= steps
        self.ptr = max(0, self.ptr)
            
        return self.history[self.ptr]

    def forward(self, steps: int) -> str:
        self.ptr += steps
        self.ptr = min(self.size - 1, self.ptr)
        
        return self.history[self.ptr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)