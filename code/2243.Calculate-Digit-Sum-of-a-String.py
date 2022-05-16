class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s_temp = []
            for i in range(0, len(s), k):
                sub_str = list(s[i:i+k])
                sub_str = [int(ss) for ss in sub_str]
                s_temp.append(str(sum(sub_str)))
            s = ''.join(s_temp)
        return s