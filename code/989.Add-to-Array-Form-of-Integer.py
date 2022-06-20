class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = [str(n) for n in num]
        num = list(str(int(''.join(num)) + k))
        return [int(n) for n in num]