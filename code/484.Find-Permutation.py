class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stack = [1]
        num = 2
        res = []
        for c in s:
            if c == 'I':
                while stack:
                    res.append(stack.pop())
           
            stack.append(num)
            num += 1

        while stack:
            res.append(stack.pop())
        
        return res
