class OrderedStream:

    def __init__(self, n: int):
        # Index starts from 1
        self.stream = [None] * (n+1)
        self.ptr = 1
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        if idKey > self.ptr:
            # Just insert, return nothing
            return []
        while self.ptr <= self.n and self.stream[self.ptr] != None:
            self.ptr += 1
        return self.stream[idKey:self.ptr]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)