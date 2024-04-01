class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        cost_table = {}
        for idx, c in enumerate(chars):
            cost_table[c] = vals[idx]

        for c in s:
            if c not in cost_table:
                cost_table[c] = ord(c) - ord('a') + 1

        # Kadane's algorithm
        max_cost = 0
        curr_cost = 0
        for c in s:
            curr_cost += cost_table[c]
            if curr_cost < 0:
                curr_cost = 0
            max_cost = max(max_cost, curr_cost)

        return max_cost
