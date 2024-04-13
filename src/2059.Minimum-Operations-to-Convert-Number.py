class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        nums = list(set(nums))
        n = len(nums)

        # bfs
        q = deque([start])
        step = 0
        visited = set([start])

        while q:
            size = len(q)
            for _ in range(size):
                curr_node = q.popleft()
                if curr_node == goal:
                    return step
                if curr_node < 0 or curr_node > 1000:
                    continue
                for i in range(n):
                    for next_node in [curr_node + nums[i], curr_node - nums[i], curr_node ^ nums[i]]:
                        if next_node in visited:
                            continue
                        visited.add(next_node)
                        q.append(next_node)

            step += 1

        return -1
