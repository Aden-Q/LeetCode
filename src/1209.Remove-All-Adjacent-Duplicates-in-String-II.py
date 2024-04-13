class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Use a stack to record the character, along with its (continuous) frequency
        # [character, frequency]
        stack = []
        
        for c in s:
            if not stack or stack[-1][0] != c:
                # Empty stack or different char
                stack.append([c, 1])
            else:
                # The stack is not empty and we find a duplicate character adjacent to it
                if stack[-1][1] == k - 1:
                    # Remove it
                    stack.pop()
                else:
                    # Otherwise increment the counter
                    stack[-1][1] += 1
                    
        res = []
        # From left to right
        for c, freq in stack:
            res.append(c * freq)
        
        return ''.join(res)