class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = len(arr) / 4
        counter = 1
        if len(arr) == 1:
            return arr[0]
        for i in range(len(arr) - 1):
            if arr[i] == arr[i+1]:
                counter += 1
            else:
                counter = 1
            if counter > freq:
                return arr[i]