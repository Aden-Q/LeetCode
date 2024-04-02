class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        n = len(arrays)
        numSets = [set(array) for array in arrays]
        print(numSets)
        # since each array is in sorted order, we don't need to consider about element order inside each array

        # O(n)
        def existInAllArrays(numSets, num: int) -> bool:
            for numSet in numSets:
                if num not in numSet:
                    return False

            return True

        ans = []
        minLenArrIndex = 0
        minArrLen = inf
        for i in range(n):
            if len(arrays[i]) < minArrLen:
                minArrLen = len(arrays[i])
                minLenArrIndex = i

        ans = []
        # O(m * n) where m is the minimum length of arrays, n is the number of arrays
        for num in arrays[minLenArrIndex]:
            if existInAllArrays(numSets, num):
                ans.append(num)

        return ans
