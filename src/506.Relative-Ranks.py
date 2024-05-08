class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = enumerate(score)
        score = sorted(score, key=lambda x: -x[1])

        res = score.copy()
        cnt = 0
        for idx, s in score:
            cnt += 1
            if cnt == 1:
                res[idx] = "Gold Medal"
            elif cnt == 2:
                res[idx] = "Silver Medal"
            elif cnt == 3:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(cnt)

        return res
