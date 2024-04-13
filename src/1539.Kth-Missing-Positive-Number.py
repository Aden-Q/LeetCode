class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # number of missing positive integer before arr[i]
        # is arr[i] - i - 1
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid - 1
        if left == 0:
            return k
        if left > len(arr) - 1:
            return arr[-1] + k - (arr[-1] - len(arr))
        return arr[left] - (arr[left] - left - k)
                