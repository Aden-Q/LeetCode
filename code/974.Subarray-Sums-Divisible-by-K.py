class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ht = {0: 1}
        prefix_sum = 0
        cnt = 0
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder in ht:
                cnt += ht[remainder]
                ht[remainder] += 1
            else:
                ht[remainder] = 1
                
        return cnt