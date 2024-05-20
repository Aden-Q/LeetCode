class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        all_subsets = []

        for num in nums:
            new_subsets = []
            for subset in all_subsets:
                new_subset = list(subset)
                new_subset.append(num)
                new_subsets.append(tuple(new_subset))
            
            all_subsets.extend(new_subsets)
            all_subsets.append((num,))
        
        res = 0
        for subset in all_subsets:
            xor = subset[0]
            for i in range(1, len(subset)):
                xor = xor ^ subset[i]
            
            res += xor

        return res
