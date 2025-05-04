class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = Counter()
        res = 0

        for first, second in dominoes:
            if first > second:
                first, second = second, first
            
            # count as we go
            res += counter[(first, second)]
            counter[(first, second)] += 1
        
        return res
