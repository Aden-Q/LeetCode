class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        table = defaultdict(int)
        # key: the prefx sum
        # value: the last index when we see this prefix sum. It's unique in this problem
        table[0] = -1
        min_lengths = [inf] * n
        prefix = 0
        min_len = inf
        for idx, num in enumerate(arr):
            if prefix - target in table:
                min_len = min(min_len, idx - 1 - table[prefix - target]) 
            
            min_lengths[idx] = min_len
            prefix += num
            table[prefix] = idx

        table = defaultdict(int)
        # key: the prefx sum
        # value: the last index when we see this prefix sum. It's unique in this problem
        table[0] = n
        postfix = 0
        min_lengths_post = [inf] * n
        min_len = inf
        for idx in range(n-1, -1, -1):
            num = arr[idx]
            postfix += num
            if postfix - target in table:
                min_len = min(min_len, table[postfix - target] - idx) 

            min_lengths_post[idx] = min_len
            table[postfix] = idx

        res = min(min_lengths_post[i] + min_lengths[i] for i in range(n))
        return res if res != inf else -1
