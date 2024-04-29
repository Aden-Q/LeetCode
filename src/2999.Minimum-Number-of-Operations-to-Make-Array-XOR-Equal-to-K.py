class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        step = 0
        num_sum = sum(nums)

        while k or num_sum:
            bit = k & 1
            currBit = nums[0] & 1
            nums[0] = nums[0] >> 1
            
            for i in range(1, len(nums)):
                currBit ^= (nums[i] & 1)
                nums[i] = nums[i] >> 1
            
            step += currBit ^ bit
            num_sum = num_sum >> 1

            k = k >> 1

        return step
