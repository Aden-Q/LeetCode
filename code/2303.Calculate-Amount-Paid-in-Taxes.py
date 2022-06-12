class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if income <= brackets[0][0]:
            return income * brackets[0][1] / 100
        idx = 0
        res = 0
        while income > 0:
            # if idx != 0:
                # print(income, res, brackets[idx][0] - brackets[idx-1][0])
            if idx == 0:
                res += brackets[idx][0] * brackets[idx][1] / 100
                income -= brackets[idx][0]
                idx += 1
                continue
            if income <= brackets[idx][0] - brackets[idx-1][0]:
                res += income * brackets[idx][1] / 100
                return res
            else:
                res += (brackets[idx][0] - brackets[idx - 1][0]) * brackets[idx][1] / 100
                income -= (brackets[idx][0] - brackets[idx - 1][0])
                idx += 1
        return res