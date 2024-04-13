class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        buckets.sort()
        total = sum(buckets)
        left, right = buckets[0], buckets[-1]
        prefixSum = [0] * (len(buckets) + 1)
        for i in range(len(buckets)):
            prefixSum[i+1] = prefixSum[i] + buckets[i]

        while (right - left) >= 1e-5:
            mid = (right - left) / 2 + left
            idx = bisect.bisect_right(buckets, mid)
            if (total - prefixSum[idx] - (len(buckets) - idx) * mid) * (1 - loss / 100) >= idx * mid - prefixSum[idx]:
                left = mid
            else:
                right = mid

        return right
