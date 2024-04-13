class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # in the first pass, we reverse the input list s
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] =s[right], s[left]
            left += 1
            right -= 1
        
        # in the second pass, we revert each word in place
        start = 0
        while start < len(s):
            length = 0
            # the deimeter is an empty char
            while start + length < len(s) and s[start+length] != ' ':
                length += 1
            # now we need to revert s[start:start+length] in place
            left, right = start, start + length - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            start = start + length + 1

        return