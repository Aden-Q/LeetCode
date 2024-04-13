class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        if sum(nums) == 0:
            return 0

        mod = 10 ** 9 + 7

        # count the number of zeros between adjacent ones
        n = len(nums)
        num_zeros_split = []
        one_index = 0
        while one_index < n and nums[one_index] != 1:
            one_index += 1

        while one_index < n:
            # find the next 1
            one_index += 1
            zeros_cnt = 0
            while one_index < n and nums[one_index] != 1:
                one_index += 1
                zeros_cnt += 1
            
            if one_index < n:
                num_zeros_split.append(zeros_cnt)

        ans = 1
        for val in num_zeros_split:
            ans = (ans * (val + 1)) % mod

        return ans
