class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        preSmaller = [-1] * len(nums)
        nextSmaller = [len(nums)] * len(nums)
        preLarger = [-1] * len(nums)
        nextLarger = [len(nums)] * len(nums)
        
        st = []
        for i in range(len(nums)):
            while len(st) > 0 and nums[st[-1]] < nums[i]:
                nextLarger[st.pop()] = i
            st.append(i)
        
        st = []
        for i in range(len(nums)):
            while len(st) > 0 and nums[st[-1]] > nums[i]:
                nextSmaller[st.pop()] = i
            st.append(i)
        
        st = []
        for i in range(len(nums) - 1, -1, -1):
            while len(st) > 0 and nums[st[-1]] >= nums[i]:
                preSmaller[st.pop()] = i
            st.append(i)
        
        st = []
        for i in range(len(nums) - 1, -1, -1):
            while len(st) > 0 and nums[st[-1]] <= nums[i]:
                preLarger[st.pop()] = i
            st.append(i)
        
        res = 0
        for i in range(len(nums)):
            res += (nextLarger[i] - i) * (i - preLarger[i]) * nums[i] - (nextSmaller[i] - i) * (i - preSmaller[i]) * nums[i]
            
        return res