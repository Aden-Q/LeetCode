class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        res = []
        [res.append(i) for i in nums1 if i not in res and i not in nums2]
        answer.append(res[:])
        res = []
        [res.append(i) for i in nums2 if i not in res and i not in nums1]
        answer.append(res[:])
        return answer