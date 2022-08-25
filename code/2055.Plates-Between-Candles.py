class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # Two array, recording the nearest candle on the left/right of position i, inclusive
        nearest_left = [-1] * len(s)
        nearest_right = [len(s)] * len(s)
        
        idx = -1
        for i in range(len(s)):
            if s[i] == '|':
                # If it is a candle, update the idx
                idx = i
            nearest_left[i] = idx
        
        idx = len(s)
        for i in range(len(s)-1, -1, -1):
            if s[i] == '|':
                idx = i
            nearest_right[i] = idx
        
        prefix_sum = [0] * len(s)
        cnt = 0
        for i in range(len(s)):
            if s[i] == '*':
                cnt += 1
            prefix_sum[i] = cnt
        
        ans = []
        for query in queries:
            left, right = query
            candle_right = nearest_left[right]
            candle_left = nearest_right[left]
            if candle_left <= right and candle_right >= left and candle_left <= candle_right:
                ans.append(prefix_sum[candle_right] - prefix_sum[candle_left])
            else:
                # No plates available for this query
                ans.append(0)
        
        return ans