class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [num - idx for idx, num in enumerate(nums)]
        # after the transformation, bad paris: paris that are not equal
        # we can count the counter part: equal pairs
        cnt_equal = 0
        counter = Counter(nums)
        for num in nums:
            cnt_equal += counter[num] - 1

        # the same pair is counted twice
        cnt_equal //= 2

        return n * (n-1) // 2 - cnt_equal
