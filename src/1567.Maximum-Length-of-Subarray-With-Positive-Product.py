class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        nums.append(0)
        left, right = 0, 0
        res = 0
        
        while left < len(nums) and right < len(nums):
            if nums[left] == 0:
                left += 1
                continue
            # left points to the first nonzero element in the list
            neg_cnt = 0
            first_neg_idx = -1
            last_neg_idx = -1
            right = left
            while nums[right] != 0:
                if nums[right] < 0:
                    if first_neg_idx == -1:
                        first_neg_idx = right
                    last_neg_idx = right
                    neg_cnt += 1
                right += 1
            if neg_cnt % 2 == 0:
                res = max(res, right - left)
            else:
                res = max(res, right - first_neg_idx - 1)
                res = max(res, last_neg_idx - left)
            left = right + 1
            
        return res