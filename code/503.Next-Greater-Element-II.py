class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        s = []
        n = len(nums)
        
        for i in range(2 * len(nums) - 1, -1, -1):
            while len(s) != 0 and s[-1] <= nums[i % n]:
                s.pop()
            res[i % n] = -1 if len(s) == 0 else s[-1]
            s.append(nums[i % n])
            
        return res