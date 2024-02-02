class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:        
        # generate a integer that has sequential digits with the leftmost number start and a fixed length
        # return -1 if impossibe
        def generateSeq(start, length):
            res = 0
            while length:
                if start == 0 or start == 10:
                    return -1
                res += start * (10 ** (length - 1))
                start += 1
                length -= 1
            
            return res

        length = len(str(low))
        first = low // (10 ** (length - 1))

        res = []
        while first * (10 ** (length - 1)) <= high:
            # generate the next integer
            num = generateSeq(first, length)
            if num == -1:
               # we need to increase the length
               length += 1
               first = 1
               continue
            elif num >= low and num <= high:
                res.append(num)

            first += 1

        return res
