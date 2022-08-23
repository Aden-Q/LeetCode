class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        hashset = set()
        
        for num in nums:
            if num > 0 and num not in hashset:
                hashset.add(num)
                cnt += 1
        
        return cnt