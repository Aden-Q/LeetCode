class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_5 = 0
        bill_10 = 0
        bill_20 = 0
        for bill in bills:
            if bill == 5:
                bill_5 += 1
            elif bill == 10:
                if bill_5 < 1:
                    return False
                else:
                    bill_5 -= 1
                    bill_10 += 1
            else:
                if bill_10 < 1:
                    if bill_5 < 3:
                        return False
                    else:
                        bill_5 -= 3
                        bill_20 += 1
                else:
                    if bill_5 < 1:
                        return False
                    else:
                        bill_10 -= 1
                        bill_5 -= 1
                        bill_20 += 1
        return True