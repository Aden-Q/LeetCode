class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ht = defaultdict(list)
        for idx, val in enumerate(nums2):
            ht[val].append(idx)

        res = [0] * len(nums1)
        for idx in range(len(nums1)):
            res[idx] = ht[nums1[idx]][-1]
            ht[nums1[idx]].pop()

        return res
