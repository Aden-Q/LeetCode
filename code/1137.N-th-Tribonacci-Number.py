class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        state1 = 0
        state2 = 1
        state3 = 1
        for _ in range(n-2):
            state1, state2, state3 = state2, state3, state1 + state2 + state3
        
        return state3