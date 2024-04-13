class HitCounter:
    def __init__(self):
        self.call_records = deque()

    def hit(self, timestamp: int) -> None:
        self.call_records.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.call_records and self.call_records[0] <= timestamp - 300:
            self.call_records.popleft()
        return len(self.call_records)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)