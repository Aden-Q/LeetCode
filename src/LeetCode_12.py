class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {}
        roman[1000] = 'M'
        roman[900] = 'CM'
        roman[500] = 'D'
        roman[400] = 'CD'
        roman[100] = 'C'
        roman[90] = 'XC'
        roman[50] = 'L'
        roman[40] = 'XL'
        roman[10] = 'X'
        roman[9] = 'IX'
        roman[5] = 'V'
        roman[4] = 'IV'
        roman[1] = 'I'
        res = ''
        num_list = list(roman.keys())
        num_list.sort(reverse = True)
        for i in num_list:
            while num >= i:
                num -= i
                res += roman[i]
            
        return res