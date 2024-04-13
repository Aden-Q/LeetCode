class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_nums = []
        neg_nums = []
        for num in nums:
            if num > 0:
                pos_nums.append(num)
            else:
                neg_nums.append(num)

        for i in range(0, len(nums), 2):
            nums[i] = pos_nums[i // 2]
            nums[i+1] = neg_nums[i // 2]
        
        return nums
