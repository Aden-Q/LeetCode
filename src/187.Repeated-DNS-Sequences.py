class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # filter out some edge cases
        if len(s) < 10:
            return []

        # now there must be at least one pattern
        # sliding window, keep the window size to be 10
        # and keep track of pattern occurance using a hashset
        # inclusive window boundary
        left, right = 0, 9
        seen = Counter()
        res = []

        while right < len(s):
            curr_str = s[left:right+1]
            if seen[curr_str] == 1:
                # we see the same pattern twice
                res.append(curr_str)
            seen[curr_str] += 1

            left += 1
            right += 1

        return res