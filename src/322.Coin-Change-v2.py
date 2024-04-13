class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # return the fewest number of contains needed to make up remain
        # using all coins
        @lru_cache(None)
        def dfs(remain):
            if remain == 0:
                return 0
            
            min_num = amount + 1
            for coin in coins:
                if coin > remain:
                    continue
                min_num = min(min_num, dfs(remain - coin) + 1)

            return min_num

        ans = dfs(amount)
        return ans if ans != amount + 1 else -1
