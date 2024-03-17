class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)
        counter = [val for val in counter.values()]
        counter.sort()
        n = len(counter)
        prefix_sum = [0] * n
        prefix_sum[0] = counter[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + counter[i]

        min_cost = inf
        for i in range(n):
            cost = prefix_sum[i-1] if i > 0 else 0
            index = bisect.bisect_right(counter, counter[i] + k)
            for j in range(index, n):
                cost += counter[j] - (counter[i] + k)
            min_cost = min(min_cost, cost)
        
        return min_cost
