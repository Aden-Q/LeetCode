from heapq import heappush, heappop

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        profits_capital = list(zip(profits, capital))
        # O(nlogn)
        profits_capital.sort(key=lambda x: x[1])
        idx = 0
        # we need a max heap by profits
        pq = []

        for _ in range(k):
            while idx < n and profits_capital[idx][1] <= w:
                # push all candidates into the max heap
                profit = profits_capital[idx][0]
                heappush(pq, -profit)
                idx += 1
            
            if pq:
                w += -heappop(pq)
            else:
                break
        
        return w
