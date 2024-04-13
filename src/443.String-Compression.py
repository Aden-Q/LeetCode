class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        # the current character that's repeating
        curr = None
        cnt = 0
        for char in chars:
            if char != curr:
                # append to the result string
                if cnt != 0:
                    res.append((curr, cnt))
                # reset
                curr = char
                cnt =  1
            else:
                # still repeating
                cnt += 1

        # append the last repeating group
        res.append((curr, cnt))

        idx = 0
        for i in range(0, len(res)):
            char, cnt = res[i]

            if cnt == 1:
                chars[idx] = char
                idx += 1
            else:
                chars[idx] = char
                idx += 1
                for c in str(cnt):
                    chars[idx] = c
                    idx += 1
            
        return idx
