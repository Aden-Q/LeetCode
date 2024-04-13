class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)

        # we want to maximize the gain by choosing k items from the gain array
        # max heap top k
        gain = [0] * n
        pq = []
        reward = 0
        for i in range(n):
            # lost if the first mouse eat the first cheese
            gain[i] = reward1[i] - reward2[i]
            reward += reward1[i]
            heapq.heappush(pq, (gain[i], i))
            if len(pq) > k:
                idx = heapq.heappop(pq)[1]
                reward += reward2[idx] - reward1[idx]

        return reward
