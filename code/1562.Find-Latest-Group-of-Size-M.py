class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m

        ans = -1
        n = len(arr)
        length = [0] * (n+2)
        for i in range(n):
            step = i + 1
            a = arr[i]
            left_len, right_len = length[a-1], length[a+1]
            if left_len == m or right_len == m:
                # last step
                ans = step - 1
            length[a-left_len] = length[a+right_len] = left_len + right_len + 1

        return ans
