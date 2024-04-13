class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # shift a input string into a base string
        # a base string is a str whose first character is 'a'
        def getBaseStr(s) -> str:
            shift = ord(s[0]) - ord('a')
            res = []
            for c in s:
                if ord(c) - shift >= ord('a'):
                    res.append(chr(ord(c) - shift))
                else:
                    res.append(chr(ord(c) - shift + 26))

            return ''.join(res)

        dt = defaultdict(list)
        for s in strings:
            base_str = getBaseStr(s)
            dt[base_str].append(s)

        return [val for val in dt.values()]
