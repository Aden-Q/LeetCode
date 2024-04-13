class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        for c in target:
            if c not in source:
                return -1

        offset = 0
        cnt = 0
        for c in target:
            # find the next match starting from the current offset
            while offset != len(source) and source[offset] != c:
                offset += 1

            if offset == len(source):
                cnt += 1
                offset = 0

            while source[offset] != c:
                offset += 1

            offset += 1
            
        return cnt + 1
