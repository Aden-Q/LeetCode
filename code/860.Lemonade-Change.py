class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5 = 0
        count10 = 0
        count20 = 0
        for bill in bills:
            if bill == 5:
                count5 += 1
            elif bill == 10:
                count10 += 1
                if count5 < 1:
                    return False
                else:
                    count5 -= 1
            elif bill == 20:
                count20 += 1
                if count10 < 1:
                    if count5 < 3:
                        return False
                    else:
                        count5 -= 3
                else:
                    count10 -= 1
                    if count5 < 1:
                        return False
                    else:
                        count5 -= 1
            
        return True