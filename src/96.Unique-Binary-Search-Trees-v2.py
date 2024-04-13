class Solution:
    def numTrees(self, n: int) -> int:
        memory = {}
        def count(low, high):
            if low >= high:
                return 1
            res = 0
            for i in range(low, high+1):
                if (low, i) not in memory:
                    c1 = count(low, i-1)
                    memory[(low, i-1)] = c1
                else:
                    c1 = memory[(low, i-1)]
                if (i+1, high) not in memory:
                    c2 = count(i+1, high)
                    memory[(i+1, high)] = c2
                else:
                    c2 = memory[(i+1, high)]
                res += c1 * c2
            return res
        
        return count(1, n)