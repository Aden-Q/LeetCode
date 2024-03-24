class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        # start: starting from to arr1[start]
        # prev: previous value
        @cache
        def dp(start, prev) -> int:
            if start == len(arr1):
                return 0
            
            cost = inf
            if arr1[start] > prev:
                cost = dp(start+1, arr1[start])

            idx = bisect.bisect_right(arr2, prev)
            if idx < len(arr2):
                cost = min(cost, 1 + dp(start+1, arr2[idx]))

            return cost

        res = dp(0, -1)
        return res if res < inf else -1
