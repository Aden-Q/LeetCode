class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for digit in num:
            while k != 0 and st and st[-1] > digit:
                st.pop()
                k -= 1
            st.append(digit)
        
        if k != 0:
            st = st[:-k]
        
        res = ''.join(st).lstrip('0')
        if not res:
            return '0'
        return res