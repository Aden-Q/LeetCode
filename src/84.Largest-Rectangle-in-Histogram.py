class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonical increasing stack
        # Find the next smaller rectangle
        next_smaller = [len(heights)] * len(heights)
        prev_smaller = [-1] * len(heights)
        mono_stack = []
        
        for idx, height in enumerate(heights):
            while mono_stack and heights[mono_stack[-1]] > height:
                next_smaller[mono_stack.pop()] = idx
            mono_stack.append(idx)
        
        mono_stack = []
        for idx in range(len(heights) - 1, -1, -1):
            height = heights[idx]
            while mono_stack and heights[mono_stack[-1]] > height:
                prev_smaller[mono_stack.pop()] = idx
            mono_stack.append(idx)
        
        res = 0
        for idx, next_smaller_idx in enumerate(heights):
            prev_smaller_idx = prev_smaller[idx]
            next_smaller_idx = next_smaller[idx]
            res = max(res, (next_smaller_idx - prev_smaller_idx - 1) * heights[idx])
        
        return res