class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        prev_num = arr[0]
        offset = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if abs(arr[i] - arr[i-1]) > abs(offset):
                offset = arr[i] - arr[i-1]
                prev_num = arr[i-1]
                break
        
        return prev_num + offset // 2
