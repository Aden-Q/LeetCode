class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        def bisect_left(arr, target, lo=0):
            left = lo
            right = n
            # [left, right)
            while left < right:
                mid = (left + right) >> 1
                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid + 1

            return left

        pivot = bisect_left(arr, x)
        ans = deque()
        left, right  = pivot-1, pivot
        while k:
            if left < 0:
                ans.append(arr[right])
                right += 1
            elif right >= n:
                ans.appendleft(arr[left])
                left -= 1
            else:
                if x - arr[left] <= arr[right] - x:
                    ans.appendleft(arr[left])
                    left -= 1
                else:
                    ans.append(arr[right])
                    right += 1
            
            k -= 1
        
        return ans
            