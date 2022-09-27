from collections import defaultdict
import heapq

class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        vals = list(self.scores.values())
        # O(K) time
        pq = vals[:K]
        heapq.heapify(pq)
        # O((N-K) log K)
        for i in range(K, len(vals)):
            heapq.heappush(pq, vals[i])
            heapq.heappop(pq)
        return sum(pq)
        
    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)