class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # right is the boundary, such that we have removed all balloons to
        # the left of colors[right] to make it colorful 
        right = 0
        stack = []
        n = len(colors)
        ans = 0
        
        while right < n:
            if stack and stack[-1][0] == colors[right]:
                # either we pop the one from the stack or discard the current one
                if neededTime[right] <= stack[-1][1]:
                    ans += neededTime[right]
                else:
                    ans += stack[-1][1]
                    stack.pop()
                    stack.append((colors[right], neededTime[right]))
            else:
                stack.append((colors[right], neededTime[right]))

            right += 1

        return ans