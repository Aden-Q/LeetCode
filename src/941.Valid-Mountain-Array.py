class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[1] < arr[0]:
            return False
        n = len(arr)
        i = 1
        while i < n and arr[i] > arr[i-1]:
            i += 1
        if i >= n:
            return False
        while i < n and arr[i] < arr[i-1]:
            i += 1
        if i == n:
            return True
        return False