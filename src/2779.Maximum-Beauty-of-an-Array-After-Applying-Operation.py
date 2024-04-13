class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ranges = []
        for num in nums:
            # inclusive ranges
            ranges.append((num-k, num+k))
        
        ranges.sort(key = lambda x: x[0])
        min_heap = []

        max_cnt = 0
        # current integer
        curr = 0
        # counts of number of overlapping intervals
        cnt = 0
        for r in ranges:
            curr = r[0]
            cnt += 1
            while min_heap and min_heap[0] < curr:
                heapq.heappop(min_heap)
                cnt -= 1

            heapq.heappush(min_heap, r[1])
            max_cnt = max(max_cnt, cnt)

        # Let N be the number of integers
        # Then there will be N ranges
        # Sorting takes O(NlogN)
        # each range will be push and pop twice
        # push and pop ops are bounded by O(log N)
        # So overall runtime is O(NlogN)
        return max_cnt