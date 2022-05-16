class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures) - 1, -1, -1):
            while len(s) != 0 and s[-1][0] <= temperatures[i]:
                s.pop()
            res[i] = 0 if len(s) == 0 else s[-1][1] - i
            s.append((temperatures[i], i))
        return res