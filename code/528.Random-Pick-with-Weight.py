class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = [0] * len(w)
        self.prefix_sum[0] = w[0]

        for i in range(1, len(w)):
            self.prefix_sum[i] = w[i] + self.prefix_sum[i-1]

        self.upper = self.prefix_sum[-1]

    def pickIndex(self) -> int:
        pivot = random.randint(0, self.upper-1)
        return bisect.bisect_right(self.prefix_sum, pivot)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()