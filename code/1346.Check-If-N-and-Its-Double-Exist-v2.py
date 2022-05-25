class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dc = {}
        for num in arr:
            if 2 * num in dc or (num % 2 == 0 and num // 2 in dc):
                return True
            dc[num] = 1
        return False