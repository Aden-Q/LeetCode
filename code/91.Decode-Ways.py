class Solution:
    def numDecodings(self, s: str) -> int:
        
        # This recursive function count different ways to decoding the string s[index:]
        @lru_cache(maxsize=None)
        def recursiveDecoding(index) -> str:
            nonlocal s
            if index == len(s):
                # reach the end of the string, only one way to decode
                return 1
            if s[index] == '0':
                # a string starting with a leading 0 cannot be decoded
                return 0
            # decode one digit
            cnt = recursiveDecoding(index + 1)
            if index < len(s) - 1 and int(s[index:index+2]) <= 26:
                # decode two digits
                cnt += recursiveDecoding(index + 2)
            return cnt
        
        return recursiveDecoding(0)