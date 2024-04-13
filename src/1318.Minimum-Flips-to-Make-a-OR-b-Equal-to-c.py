class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0
        while c:
            c_last_bit = c & 1
            a_last_bit = a & 1
            b_last_bit = b & 1
            if not c_last_bit:
                cnt += a_last_bit + b_last_bit
            else:
                cnt += 1 if not (a_last_bit + b_last_bit) else 0

            c = c >> 1
            b = b >> 1
            a = a >> 1
        
        while a:
            cnt += 1
            a = a & (a-1)
        
        while b:
            cnt += 1
            b = b & (b-1)
        
        return cnt