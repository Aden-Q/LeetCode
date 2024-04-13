class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        ans = 0
        for num in set(nums):
            # check whether we have (num + k) to remove duplicates
            if k == 0:
                if counter[num] > 1:
                    ans += 1
            else:
                if counter[num + k] > 0:
                    ans += 1
        
        return ans
