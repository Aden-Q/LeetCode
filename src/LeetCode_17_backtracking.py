class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_dict = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        path = ""  # a single path
        res = []  # final solution
        # make digits global and only pass the start index to reduce memory consumption
        def backtracking(cur):
            nonlocal path
            nonlocal res
            nonlocal map_dict
            # terminate condition
            if len(path) == len(digits):
                res.append(path)
                return
            # process nodes
            for c in map_dict[digits[cur]]:
                path += c
                backtracking(cur+1)
                path = path[:-1]
            
        if digits == "":
            return []
        else:
            backtracking(0)
            return res