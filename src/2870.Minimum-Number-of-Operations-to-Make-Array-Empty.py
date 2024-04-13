class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for freq in counter.values():
            if freq % 3 == 0:
                ans += freq // 3
            elif freq % 3 == 2:
                ans += freq // 3 + 1
            else:
                if freq == 1:
                    return -1
                ans += freq // 3 + 1
                
        return ans