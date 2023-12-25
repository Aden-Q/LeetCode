class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        ops = 0

        for num in nums:
            complement = k - num
            if complement not in counter:
                counter[num] += 1
            else:
                ops += 1
                counter[complement] -= 1
                if counter[complement] == 0:
                    del counter[complement]

        return ops