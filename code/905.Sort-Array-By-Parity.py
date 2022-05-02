class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res_even = []
        res_odd = []
        for num in nums:
            if num % 2 == 0:
                res_even.append(num)
            else:
                res_odd.append(num)
                
        res_even.extend(res_odd)
        return res_even