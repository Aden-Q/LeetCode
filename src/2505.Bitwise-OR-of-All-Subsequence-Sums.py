class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        carry = 0
        total = sum(nums)
        offset = 0
        res = 0
        
        while total:
            numSetBits = 0
            for i in range(len(nums)):
                numSetBits += nums[i] & 1
                nums[i] = nums[i] >> 1
            
            if numSetBits + carry > 0:
                res |= (1 << offset)

            carry = (numSetBits + carry) >> 1

            offset += 1
            total = total >> 1

        return res
