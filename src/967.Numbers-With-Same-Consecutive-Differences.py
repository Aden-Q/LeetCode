class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        path = []
        
        def dfs(num_digit, cur_digit):
            if num_digit == n-1:
                res.append(int(''.join(path)))
                return
            next_digit_candidate = [cur_digit] if k == 0 else [cur_digit + k, cur_digit - k]
            for next_digit in next_digit_candidate:
                if next_digit < 10 and next_digit >= 0:
                    path.append('%d' % next_digit)
                    dfs(num_digit + 1, next_digit)
                    path.pop()
            return
        
        for i in range(1, 10):
            path = ['%d' % i]
            dfs(0, i)
            
        return res    