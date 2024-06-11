class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        table = {}
        for idx, val in enumerate(arr2):
            table[val] = idx

        for val in arr1:
            if val not in table:
                table[val] = len(arr2) + val

        return sorted(arr1, key=lambda x: table[x])
