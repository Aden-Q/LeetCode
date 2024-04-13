class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        
        # test whether x can be an answer to the problem
        def isWorkable(x) -> bool:
            nonlocal sweetness, k

            currSweetness = 0
            numCut = 0
            for sweet in sweetness:
                currSweetness += sweet
                if currSweetness >= x:
                    # reset and perform the next cut
                    numCut += 1
                    currSweetness = 0

            if numCut >= k + 1:
                return True

            return False

        # search boundary [left, right)
        left, right = 0, sum(sweetness) + 1
        while left < right:
            mid = (right - left) // 2 + left
            # now we search for mid
            if isWorkable(mid):
                left = mid + 1
            else:
                right = mid

        return left - 1
