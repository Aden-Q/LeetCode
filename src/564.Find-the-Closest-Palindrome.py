class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def isAllNine(s) -> bool:
            for c in s:
                if c != '9':
                    return False
            
            return True
        
        def isPalindrom(s) -> bool:
            left, right = 0, len(n) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        if int(n) <= 10 or (n[0] == '1' and int(n) % 10 == 0 and int(n[1:]) == 0):
            return str(int(n) - 1)

        if int(n) == 11 or (n[0] == '1' and n[-1] == '1' and int(n[1:-1]) == 0):
            return str(int(n) - 2)

        if isAllNine(n):
            return str(int(n) + 2)

        candidates = set()
        if len(n) % 2 == 0:
            firstHalf = n[:len(n) // 2]
            firstHalfIncr = str(int(firstHalf) + 1)
            candidates.add(firstHalfIncr + firstHalfIncr[::-1])
            firstHalfDecr = str(int(firstHalf) - 1)
            candidates.add(firstHalfDecr + firstHalfDecr[::-1])
            if not isPalindrom(n):
                candidates.add(firstHalf + firstHalf[::-1])
        else:
            firstHalf =  n[:len(n) // 2 + 1]
            firstHalfIncr = str(int(firstHalf) + 1)
            candidates.add(firstHalfIncr + firstHalfIncr[::-1][1:])
            firstHalfDecr = str(int(firstHalf) - 1)
            candidates.add(firstHalfDecr + firstHalfDecr[::-1][1:])
            if not isPalindrom(n):
                candidates.add(firstHalf + firstHalf[::-1][1:])

        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
