class FirstUnique:
    def __init__(self, nums: List[int]):
        self.counter = Counter(nums)
        self.q = deque()
        for num in nums:
            if self.counter[num] == 1:
                self.q.append(num)

    def showFirstUnique(self) -> int:
        while self.q and self.counter[self.q[0]] > 1:
            # remove those duplicates from the queue
            self.q.popleft()

        return self.q[0] if self.q else -1

    def add(self, value: int) -> None:
        if value in self.counter:
            self.counter[value] += 1
        else:
            # new element
            self.counter[value] = 1
            self.q.append(value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)