class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n = len(picture), len(picture[0])
        # map row index to col indices of B's
        ht_row = defaultdict(list)
        # map col index to row indices of B's
        ht_col = defaultdict(list)
        for row in range(m):
            for col in range(n):
                if picture[row][col] == 'B':
                    ht_row[row].append(col)
                    ht_col[col].append(row)
        
        res = 0
        for key in ht_row:
            if len(ht_row[key]) > 1:
                # there are more than 1 B's in the current row
                continue
            if len(ht_col[ht_row[key][0]]) != 1:
                continue
            res += 1

        return res
