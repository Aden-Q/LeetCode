class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # O(n) solution
        # left scan + right scan
        ht_left = {}
        ans = [0] * len(nums)
        for idx, num in enumerate(nums):
            if num in ht_left:
                prefix_sum, cnt = ht_left[num]
                ans[idx] += cnt * idx - prefix_sum
                ht_left[num] = (prefix_sum + idx, cnt + 1)
            else:
                ht_left[num] = (idx, 1)
        
        ht_right = {}
        for idx in range(len(nums)-1, -1, -1):
            num = nums[idx]
            if num in ht_right:
                prefix_sum, cnt = ht_right[num]
                ans[idx] += prefix_sum - cnt * idx
                ht_right[num] = (prefix_sum + idx, cnt + 1)
            else:
                ht_right[num] = (idx, 1)

        return ans
