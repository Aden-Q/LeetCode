from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        length = len(arr)
        visited = [False] * length
        
        # Run BFS
        q = deque([start])
        visited[start] = True
        if arr[start] == 0:
            return True
        while q:
            sz = len(q)
            for _ in range(sz):
                cur_pos = q.popleft()
                for next_pos in [cur_pos + arr[cur_pos], cur_pos - arr[cur_pos]]:
                    if next_pos >= length or next_pos < 0:
                        # We cannot jump outside of the array
                        continue
                    if not visited[next_pos]:
                        # Early termination if we reach
                        # a position with a 0 value
                        if arr[next_pos] == 0:
                            return True
                        visited[next_pos] = True
                        q.append(next_pos)
        
        # Check whether all enries with value 0 is visited
        return False    