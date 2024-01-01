class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n, m = len(workers), len(bikes)
        min_total_dist = math.inf

        # an hashset indicating which bikes have been used so far
        used = set()
        # we are currently assigning some bike to worker i
        # j: the current bike assigned to worker i
        # curr_sum is the culmulative sum of manhattan distance so far
        def dfs(i, j, curr_sum) -> None:
            nonlocal used, min_total_dist
            if i == n:
                # out of the boundary
                return

            used.add(j)
            new_sum = curr_sum + abs(bikes[j][0] - workers[i][0]) + abs(bikes[j][1] - workers[i][1])
            if new_sum >= min_total_dist:
                # trim the search space
                used.remove(j)
                return

            if i == n - 1:
                min_total_dist = min(min_total_dist, new_sum)

            # otherwise we explore the current worker
            for bike_idx in range(m):
                if bike_idx in used:
                    continue
                dfs(i+1, bike_idx, new_sum)

            used.remove(j)
            return

        for j in range(m):
            dfs(0, j, 0)
        return min_total_dist