class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        counter1 = 0
        counter2 = 0
        ptr1 = len(s) - 1
        ptr2 = len(t) - 1
        while ptr1 >= 0 and ptr2 >= 0:
            while ptr1 >= 0:
                if s[ptr1] == '#':
                    counter1 += 1
                    ptr1 -= 1
                elif counter1 > 0:
                    ptr1 -= 1
                    counter1 -= 1
                else:
                    # in this case, we find the first entry to compare
                    break
            while ptr2 >= 0:
                if t[ptr2] == '#':
                    counter2 += 1
                    ptr2 -= 1
                elif counter2 > 0:
                    ptr2 -= 1
                    counter2 -= 1
                else:
                    # in this case, we find the first entry to compare
                    break
            if ptr1 >= 0 and ptr2 >= 0:
                if s[ptr1] != t[ptr2]:
                    return False
                else:
                    # move backwards
                    ptr1 -= 1
                    ptr2 -= 1
            elif ptr1 >= 0 or ptr2 >= 0:
                return False
        return True     