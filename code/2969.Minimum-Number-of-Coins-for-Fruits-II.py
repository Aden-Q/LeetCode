from heapq import heappush, heappop

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        # (cost, index), representing the minimum cost if we collect all fruits starting from index and buying the current fruit
        pq = [(0, n)]
        ans = 0
        for i in range(n-1, -1, -1):
            while pq and pq[0][1] > 2 * i + 2:
                heappop(pq)

            heappush(pq, (pq[0][0] + prices[i], i))

        return pq[0][0] + prices[i]
