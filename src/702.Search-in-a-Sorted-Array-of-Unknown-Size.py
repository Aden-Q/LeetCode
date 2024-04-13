# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        # the max index is 10**4 - 1
        # search space [left, right)
        sentinel = 2 ** 31 -1
        left, right = 0, 10 ** 4
        while left < right:
            mid = (right - left) // 2 + left
            query_res = reader.get(mid)
            if query_res == sentinel:
                right = mid
            if query_res == target:
                return mid
            elif query_res < target:
                left = mid + 1
            else:
                right = mid

        return left if reader.get(left) == target else -1
