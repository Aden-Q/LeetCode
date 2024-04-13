class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        
        def binary_search(arr, num):
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] == num:
                    return mid
                elif arr[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        count = 0
        for num in arr1:
            idx = binary_search(arr2, num)
            if idx == 0:
                if abs(num - arr2[idx]) > d:
                    count += 1
            elif idx == len(arr2):
                if abs(num - arr2[idx-1]) > d:
                    count += 1
            else:
                if min(abs(num - arr2[idx]), abs(num - arr2[idx-1])) > d:
                    count += 1
        return count