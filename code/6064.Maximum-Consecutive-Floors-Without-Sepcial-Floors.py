class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        max_count = max(special[0] - bottom, top - special[-1])
        for i in range(len(special) - 1):
            max_count = max(max_count, special[i+1] - special[i] - 1)
        return max_count