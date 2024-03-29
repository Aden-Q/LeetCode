class Solution:
    def combine(self, str1, str2):
        res = []
        if len(str1) == 0:
            return str2
        elif len(str2) == 0:
            return str1
        for s1 in str1:
            for s2 in str2:
                res.append(s1+s2)
        return res
    
    
    def recursive_append(self, digits_str, map_dict):
        '''This method combines two list of strings
        '''
        if len(digits_str) == 0:
            return []
        elif len(digits_str) == 1:
            return map_dict[digits_str[0]]
        else:
            return self.combine(map_dict[digits_str[0]], self.recursive_append(digits_str[1:], map_dict))
            
    def letterCombinations(self, digits: str):
        import string
        alphabete = string.ascii_lowercase
        map_dict = {}
        map_dict['2'] = list("abc")
        map_dict['3'] = list("def")
        map_dict['4'] = list("ghi")
        map_dict['5'] = list("jkl")
        map_dict['6'] = list("mno")
        map_dict['7'] = list("pqrs")
        map_dict['8'] = list("tuv")
        map_dict['9'] = list("wxyz")
        
        return self.recursive_append(digits, map_dict)
        