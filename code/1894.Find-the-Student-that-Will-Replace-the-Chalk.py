class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        target = k % (sum(chalk))
        left = 0
        while target >= chalk[left]:
            target -= chalk[left]
            left += 1
        return left