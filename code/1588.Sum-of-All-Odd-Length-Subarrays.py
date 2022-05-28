class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix_sum = [0] * (len(arr) + 1)
        res = 0
        for i in range(len(arr)):
            prefix_sum[i+1] = prefix_sum[i] + arr[i]
        for length in range(1, len(arr)+1, 2):
            for start_point in range(len(arr) - length + 1):
                res += prefix_sum[start_point+length] - prefix_sum[start_point]
        return res