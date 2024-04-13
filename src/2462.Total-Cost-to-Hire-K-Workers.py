class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # we can maintain two min heaps, each of which has a size at most candidates
        # at most k because we don't want to push the same candidate into both heaps
        # this can save some time and space
        n = len(costs)
        # left is the next position of the element to be inserted into the left min heap
        # right is the next position of the element to be inserted into the right min heap
        left, right = candidates - 1, n - candidates
        if left >= right:
            left = n // 2
            right = n // 2 + 1

        left_min_heap = [costs[idx] for idx in range(left+1)]
        heapq.heapify(left_min_heap)
        right_min_heap = [costs[idx] for idx in range(right, n)]
        heapq.heapify(right_min_heap)

        ans = 0
        for _ in range(k):
            left_min_val = math.inf
            if left_min_heap:
                left_min_val = left_min_heap[0]
            
            right_min_val = math.inf
            if right_min_heap:
                right_min_val = right_min_heap[0]

            if left_min_val <= right_min_val:
                # pop from the left
                heapq.heappop(left_min_heap)
                ans += left_min_val
                if left + 1 < right:
                    left += 1
                    # push
                    heapq.heappush(left_min_heap, costs[left])
            else:
                # pop from the left
                heapq.heappop(right_min_heap)
                ans += right_min_val
                if right - 1 > left:
                    right -= 1
                    # push
                    heapq.heappush(right_min_heap, costs[right])

        return ans