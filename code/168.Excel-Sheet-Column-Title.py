class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        
        while columnNumber != 0:
            res.append(chr(ord('A') + (columnNumber - 1) % 26))
            columnNumber = (columnNumber - 1) // 26
        
        return ''.join(res[::-1])