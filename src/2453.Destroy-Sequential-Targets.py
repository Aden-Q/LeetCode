class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort(reverse=True)
        # a map from a number to the maximum number of targets that can be destroyed if the machine is seeded with this number
        # we take the key to mod space
        dp = defaultdict(int)
        max_num_targets = 0
        seed = 0
        for num in nums:
            num_mod_space = num % space
            dp[num_mod_space] += 1
            # update the answer
            if dp[num_mod_space] >= max_num_targets:
                max_num_targets = dp[num_mod_space]
                seed = num

        return seed
