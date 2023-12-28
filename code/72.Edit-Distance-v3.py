class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        m, n = len(word1), len(word2)

        if m == 0:
            return n
        if n == 0:
            return m

        prev_row = list(range(n+1))
        curr_row = list(range(n+1))

        for row in range(1, m+1):
            curr_row[0] = row
            for col in range(1, n+1):
                if word1[row-1] == word2[col-1]:
                    curr_row[col] = prev_row[col-1]
                else:
                    replace_dist = prev_row[col-1]
                    insert_dist = curr_row[col-1]
                    delete_dist = prev_row[col]
                    curr_row[col] = min(replace_dist, insert_dist, delete_dist) + 1

            # to avoid garbage collector to collect the old prev_row
            prev_row, curr_row = curr_row, prev_row

        return prev_row[-1]
