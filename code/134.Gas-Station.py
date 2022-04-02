class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rest = []
        for i in range(len(gas)):
            rest.append(gas[i] - cost[i])
        if sum(rest) < 0:
            return -1
        start_idx = 0
        count = 0
        cur_sum = 0
        while count < len(rest):
            cur_sum += rest[(start_idx + count) % len(rest)]
            count += 1
            if cur_sum < 0:
                # reset
                cur_sum = 0
                start_idx = (start_idx + count) % len(rest)
                count = 0
        return start_idx    