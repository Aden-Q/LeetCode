from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        q = deque()
        q.append(0)
        visited[0] = True
        while len(q) != 0:
            sz = len(q)
            for _ in range(sz):
                cur_room = q.popleft()
                for next_room in rooms[cur_room]:
                    if not visited[next_room]:
                        visited[next_room] = True
                        q.append(next_room)
        for v in visited:
            if v == False:
                return False
        return True