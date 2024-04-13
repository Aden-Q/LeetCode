class Solution:
    def minOperations(self, k: int) -> int:
        curr_max = 1
        steps = inf
        
        while curr_max < k:
            num_duplicates = ceil(k / curr_max) - 1
            steps = min(steps, num_duplicates + curr_max - 1)
            curr_max += 1
            
        return steps if steps != inf else 0
