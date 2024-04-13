class RecentCounter:
    def __init__(self):
        self.time_queue = []

    def ping(self, t: int) -> int:
        self.time_queue.append(t)

        # binary search the start position
        idx = bisect.bisect_left(self.time_queue, t-3000)
        return len(self.time_queue) - idx

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)