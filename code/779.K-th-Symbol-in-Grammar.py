class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # index starts from 1
        if n == 1:
            return 0
        return k % 2 if self.kthGrammar(n-1, (k + 1) // 2) else 1 - k % 2