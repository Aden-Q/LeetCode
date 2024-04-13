class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProd = [1] * (n + 1)
        suffixProd = [1] * (n + 1)

        # valid: prefixProd[1:]
        for i in range(n):
            prefixProd[i+1] = prefixProd[i] * nums[i]
        
        # valid: suffixProd[1:]
        for i in range(n):
            suffixProd[i+1]= suffixProd[i] * nums[n-1-i]
        
        return [prefixProd[i] * suffixProd[n-1-i] for i in range(n)]