class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        len1 = len(pattern)
        s = s.split()
        len2 = len(s)
        if len1 != len2:
            return False
        dict1 = {}
        res1 = []
        dict2 = {}
        res2 = []
        count = 0
        for i in range(len1):
            if dict1.get(pattern[i]) == None:
                dict1[pattern[i]] = count
                res1.append(count)
                count += 1
            else:
                res1.append(dict1[pattern[i]])
        count = 0
        for i in range(len1):
            if dict2.get(s[i]) == None:
                dict2[s[i]] = count
                res2.append(count)
                count += 1
            else:
                res2.append(dict2[s[i]])
        return res1 == res2