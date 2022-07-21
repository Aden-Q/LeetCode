import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []
        
        for r in range(min(n, k)):
            min_heap.append((matrix[r][0], r, 0))
            
        heapq.heapify(min_heap)
            
        for _ in range(k):
            cur, r, idx = heapq.heappop(min_heap)
            if idx < len(matrix[r]) - 1:
                heapq.heappush(min_heap, (matrix[r][idx+1], r, idx+1))
            # if the current row is exhausted, do nothing
        return cur  