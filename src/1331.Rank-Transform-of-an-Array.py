class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []
        arr_sort = [(val, idx) for idx, val in enumerate(arr)]
        arr_sort.sort(key = lambda x : x[0])
        res = [0] * len(arr)
        res[arr_sort[0][1]] = 1
        
        rank = 1
        idx = 1
        while idx < len(arr_sort):
            if arr_sort[idx][0] != arr_sort[idx-1][0]:
                rank += 1
            res[arr_sort[idx][1]] = rank
            idx += 1
        
        return res