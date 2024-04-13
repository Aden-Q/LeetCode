class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        right_shift_total = 0
        for d, amount in shift:
            if d == 1:
                right_shift_total += amount
            else:
                right_shift_total -= amount
            
        right_shift_total = right_shift_total % len(s)
        
        return s[-right_shift_total:] + s[:-right_shift_total]
