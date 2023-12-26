class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # count the total number of rooms visited
        cnt = 0
        n = len(rooms)
        visited = [False] * n
        # pos is the current root number (0-index)
        def dfs(pos) -> None:
            nonlocal cnt
            # skip if we have visited the current room
            if visited[pos]:
                return

            cnt += 1
            visited[pos] = True
            for next_room in rooms[pos]:
                dfs(next_room)

            return            
        
        # start from room 0
        dfs(0)
        if cnt == n:
            return True
        
        return False