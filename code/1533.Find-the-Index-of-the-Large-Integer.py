# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        # binary search, obvious
        # search range: [left, right)
        left, right = 0, n
        while left + 1 < right:
            mid = (right - left) // 2 + left
            if (right - left) % 2 == 0:
                # we can split it equally
                # [left...mid-1]
                # [mid...right]
                compare = reader.compareSub(left, mid-1, mid, right-1)
                if compare == 1:
                    right = mid
                else:
                    left = mid
            else:
                # we can split it equally
                # [left...mid-1]
                # [mid+1...right]
                # and there's one number left
                compare = reader.compareSub(left, mid-1, mid+1, right-1)
                if compare == 0:
                    return mid
                elif compare == 1:
                    right = mid
                else:
                    left = mid + 1

        return left
