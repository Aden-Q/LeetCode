class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # return a list of numbers of length n
        def dp(n: int) -> list[str]:
            if n == 1:
                return ["0","1","8"]
            if n == 2:
                return ["11","69","88","96"]

            res = []
            if n % 2 == 1:
                prev_nums = dp(n-1)
                for num in prev_nums:
                    split = len(num) // 2
                    for c in ['0', '1', '8']:
                        res.append(num[:split] + c + num[split:])
            else:
                prev_nums = dp(n-2)
                for num in prev_nums:
                    split = len(num) // 2
                    for c in ['00', '11', '69', '88', '96']:
                        res.append(num[:split] + c + num[split:])

            return res

        return dp(n)
