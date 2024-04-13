class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_dict = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        digits = [int(digit) for digit in digits]
        size = len(digits)
        res = []
        path = []
        if len(digits) == 0:
            return []
        
        def traverse(start):
            nonlocal map_dict, digits, size
            if len(path) == size:
                res.append(''.join(path))
                return
            for c in map_dict[digits[start]]:
                path.append(c)
                traverse(start + 1)
                path.pop()
            return
        
        traverse(0)
        return res