class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        ans = []
        if intLength % 2 == 0:
            base = 10**(intLength // 2 - 1)
            for i in queries:
                temp = base + i - 1
                if temp > base * 10 - 1:
                    ans.append(-1)
                else:
                    temp = str(temp)
                    temp = temp + temp[::-1]
                    ans.append(int(temp))
        else:
            base = 10**(intLength // 2)
            for i in queries:
                temp = base + i - 1
                if temp > base * 10 - 1:
                    ans.append(-1)
                else:
                    temp = str(temp)
                    temp = temp + temp[:-1:][::-1]
                    ans.append(int(temp))
        return ans