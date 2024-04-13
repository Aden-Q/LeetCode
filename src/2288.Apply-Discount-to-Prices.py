class Solution:
    def isPrice(self, s) -> bool:
        for c in s:
            if not c.isdigit():
                return False
        return True
        
        
    def discountPrices(self, sentence: str, discount: int) -> str:
        sentence = sentence.split()
        res = []
        for s in sentence:
            if s[0] != '$' or len(s) == 1:
                res.append(s)
            elif self.isPrice(s[1:]):
                # is a price
                res.append('$%.2f' % (float(s[1:]) * (100-discount) / 100))
            else:
                res.append(s)
        return ' '.join(res)   