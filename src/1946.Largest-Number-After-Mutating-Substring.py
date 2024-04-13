class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        # straightforward greedy algorithm
        num_str = list(num)
        start_idx = 0
        while start_idx < len(num_str) and change[int(num_str[start_idx])] <= int(num_str[start_idx]):
            start_idx += 1

        for idx in range(start_idx, len(num_str)):
            digit = int(num_str[idx])
            if change[digit] >= digit:
                num_str[idx] = str(change[digit])
            else:
                break

        return ''.join(num_str)
