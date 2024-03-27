class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        ans = []
        visited = set()

        minHeap = [(nums1[0] + nums2[0], 0, 0)]
        visited.add((0, 0))
        
        while len(ans) < k:
            currSum, idx1, idx2 = heapq.heappop(minHeap)
            ans.append([nums1[idx1], nums2[idx2]])
            
            if idx1 + 1 < m and (idx1+1, idx2) not in visited:
                heapq.heappush(minHeap, (nums1[idx1+1] + nums2[idx2], idx1+1, idx2))
                visited.add((idx1+1, idx2))
            
            if idx2 + 1 < n and (idx1, idx2+1) not in visited:
                heapq.heappush(minHeap, (nums1[idx1] + nums2[idx2+1], idx1, idx2+1))
                visited.add((idx1, idx2+1))

        return ans
