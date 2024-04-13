class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort(reverse=True)
        n = len(beans)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + beans[i]
        
        minCost = inf
        currCost = 0
        for i in range(n-1, -1, -1):
            # check whether we remove all or keep it as it is
            # if we keep it
            minCost = min(minCost, currCost + prefixSum[i] -  beans[i] * i)
            # if we remove it
            currCost += beans[i]

        minCost = min(minCost, currCost)
        return minCost
