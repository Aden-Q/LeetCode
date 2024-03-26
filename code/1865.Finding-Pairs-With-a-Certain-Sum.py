class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1.copy()
        # make a copy we don't modify the input
        self.nums2 = nums2.copy()
        self.counter = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        # O(1)
        self.counter[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.counter[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for num in self.nums1:
            ans += self.counter[tot - num]
        
        return ans
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)