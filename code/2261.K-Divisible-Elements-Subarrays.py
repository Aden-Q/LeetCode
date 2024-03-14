class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        # use a hashset to uniquely identify some subarray that satisfies the requirement
        # the answer is the length of this set
        ans_set = set()
        n = len(nums)
        left = right = 0
        num_divisible_by_p = 0

        # sliding window
        while right < n:
            if nums[right] % p == 0:
                num_divisible_by_p += 1

            while num_divisible_by_p > k:
                if nums[left] % p == 0:
                    num_divisible_by_p -= 1
                left += 1
            
            for start in range(left, right+1):
                ans_set.add(tuple(nums[start:right+1]))

            right += 1

        return len(ans_set)
