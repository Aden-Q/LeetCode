class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        ht = {}
        
        for idx, c in enumerate(s):
            if c == '(':
                st.append(idx)
            elif c == ')':
                ht[st.pop()] = idx
        
        res = []
        s_cur = s
        # reverse for each pair of paratheses
        for left_idx, right_idx in ht.items():
            s_cur = s_cur[:left_idx+1] + s_cur[left_idx+1:right_idx][::-1] + s_cur[right_idx:]
        # remove paratheses
        res = []
        for c in s_cur:
            if c not in ['(', ')']:
                res.append(c)
                
        return ''.join(res)
            
                