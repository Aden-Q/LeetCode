class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        # Two pointers, two run
        n = len(nums)
        res = 0
        # First prefix sum
        # prefixSum[i+1] = nums[0] + nums[1] + ... + nums[i]
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i+1] = prefixSum[i] + nums[i]
        
        for i in range(n):
            first_start, first_end = i, i + firstLen - 1
            if first_end >= n:
                continue
            for j in range(n):
                # i: start of the first
                # j: start of the second
                second_start, second_end = j, j + secondLen - 1
                if second_end >= n:
                    continue
                if second_start >= first_start and second_start <= first_end:
                    continue
                if first_start >= second_start and first_start <= second_end:
                    continue
                res = max(res, prefixSum[first_end + 1] - prefixSum[first_start] + prefixSum[second_end + 1] - prefixSum[second_start])
        
        return res