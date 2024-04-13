class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        # The current position
        cur = 0
        cnt = 0
        # Use greedy algorithm to determine where to jump next
        while cur < length - 1:
            # Make a jump
            cnt += 1
            next_max = cur + nums[cur]
            if next_max >= length - 1:
                # If we can jump to the end starting from the current position
                return cnt
            # Otherwise determine the next optimal jumping position
            next_pos = cur + 1
            cur_val = -1
            for j in range(cur + 1, next_max + 1):
                if j + nums[j] > cur_val:
                    cur_val = j + nums[j]
                    next_pos = j
            cur = next_pos

        return cnt