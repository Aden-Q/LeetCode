class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        
        for c in s:
            st.append(c)
            if c == ']':
                cur_str = ''
                while not st[-1].isdigit():
                    cur_str = st.pop() + cur_str
                digits = ''
                while st and st[-1].isdigit():
                    digits = st.pop() + digits
                cur_str = int(digits) * cur_str[1:-1]
                st.append(cur_str)
                
        return ''.join(st)