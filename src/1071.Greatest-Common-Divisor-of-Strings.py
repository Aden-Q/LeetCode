class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1

        gcd_len = len(str1)
        for i in range(1, len(str1) + 1):
            if len(str1) % i != 0:
                continue
            gcd_len = len(str1) // i
            if len(str2) % gcd_len != 0:
                continue

            pattern = str1[:gcd_len]
            if str1 != pattern * i:
                continue
            if str2 != pattern * (len(str2) // gcd_len):
                continue
            
            return pattern

        return ""