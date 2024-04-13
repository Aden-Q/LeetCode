import random
class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.block_dict = {i:0 for i in blacklist}
        self.size = n - len(blacklist)
        last = n - 1
        for num in blacklist:
            if num >= self.size:
                continue
            while self.block_dict.get(last) != None:
                last -= 1
            self.block_dict[num] = last
            last -= 1

    def pick(self) -> int:
        idx = random.randint(0, self.size - 1)
        if self.block_dict.get(idx) != None:
            return self.block_dict[idx]
        return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()