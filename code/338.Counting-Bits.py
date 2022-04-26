class Solution:
    def countOnes(self, n):
        count = 0
        while n != 0:
            if n % 2 == 1:
                count += 1
            n = n // 2
        return count
    
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            res.append(self.countOnes(i))
        return res