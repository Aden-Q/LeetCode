class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ht = Counter()
        ans = 0
        for num in nums:
            ans += ht[num - k]
            ht[num] += 1
        
        return ans
