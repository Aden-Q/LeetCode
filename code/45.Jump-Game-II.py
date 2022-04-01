class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        cur_pos = 0
        next_pos = 0
        count = 0
        max_val = 0
        while cur_pos + nums[cur_pos] < len(nums) - 1:
            max_val = 0
            for i in range(cur_pos, cur_pos + nums[cur_pos] + 1):
                if i + nums[i] > max_val:
                    max_val = nums[i] + i
                    next_pos = i
            cur_pos = next_pos
            count += 1
        return count + 1