class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # we first sort all pairs by their ending time, ascendingly
        pairs.sort(key = lambda x: x[1])

        # then we intelligently build the chain by selecting pairs from left to right
        ans = 1
        curr_end = pairs[0][1]
        for idx in range(1,len(pairs)):
            if pairs[idx][0] <= curr_end:
                continue
            ans += 1
            curr_end = pairs[idx][1]
        
        return ans
