class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        index_lookup = {val: idx for idx, val in enumerate(target)}

        # now we need to find the length of the LIS in arr_converted
        sub = []
        for num in arr:
            if num not in index_lookup:
                continue
            idx = bisect.bisect_left(sub, index_lookup[num])
            if idx == len(sub):
                sub.append(index_lookup[num])
            else:
                # replace
                sub[idx] = index_lookup[num]

        return len(target) - len(sub)
