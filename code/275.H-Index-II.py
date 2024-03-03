class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def feasible(citation):
            left, right = 0, len(citations)
            while left < right:
                mid = left + (right - left) // 2
                if citations[mid] < citation:
                    left = mid + 1
                else:
                    right = mid
            
            return len(citations) - left >= citation

        # obvious binary search problem
        left, right = 0, 1000
        while left < right:
            mid = left + (right - left) // 2
            # search for the minimum citations such that >= mid
            if feasible(mid):
                left = mid + 1
            else:
                right = mid

        return left - 1 if left > 0 else 0
