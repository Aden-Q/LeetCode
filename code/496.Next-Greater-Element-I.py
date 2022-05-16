class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        s = []
        
        for i in range(len(nums2) - 1, -1, -1):
            while len(s) != 0 and s[-1] < nums2[i]:
                s.pop()
            res[nums2[i]] = -1 if len(s) == 0 else s[-1]
            s.append(nums2[i])
            
        ans = []
        for num in nums1:
            ans.append(res[num])
        return ans