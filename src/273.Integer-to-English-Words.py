class Solution:
    def numberToWords(self, num: int) -> str:
        # this is a special case and the only case we need to print zero
        if num == 0:
            return "Zero"

        res = deque()

        table = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }

        # how many billion, 1 or 2
        num_billion = num // 10 ** 9
        if num_billion > 0:
            res.append(table[num_billion] + " Billion")

        num = num % 10 ** 9

        # how many million, 1 to 999
        has_million = num >= 10 ** 6
        num_million = num // 10 ** 6
        # hwo many hundred million
        if num_million > 99:
            res.append(table[num_million // 100] + " Hundred")

        num_million -= num_million // 100 * 100
        
        if num_million > 19:
            res.append(table[num_million // 10 * 10])
            num_million -= num_million // 10 * 10

        if num_million > 0:
            res.append(table[num_million])

        if has_million:
            res.append("Million")

        num = num % 10 ** 6

        # how many thousand, 1 to 999
        has_thousand = num >= 10 ** 3
        num_thousand = num // 10 ** 3
        # hwo many hundred thousand
        if num_thousand > 99:
            res.append(table[num_thousand // 100] + " Hundred")

        num_thousand -= num_thousand // 100 * 100
        
        if num_thousand > 19:
            res.append(table[num_thousand // 10 * 10])
            num_thousand -= num_thousand // 10 * 10

        if num_thousand > 0:
            res.append(table[num_thousand])

        if has_thousand:
            res.append("Thousand")

        num = num % 10 ** 3

        # below than 1k
        has_remaining = num > 0
        if num > 99:
            res.append(table[num // 100] + " Hundred")

        num = num % 100

        if num > 19:
            res.append(table[num // 10 * 10])
            num -= num // 10 * 10

        if num > 0:
            res.append(table[num])

        return ' '.join(res)
