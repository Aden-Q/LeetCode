from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def getUp(s, pos):
            s_list = list(s)
            if s_list[pos] == '9':
                s_list[pos] = '0'
            else:
                s_list[pos] = str(int(s_list[pos]) + 1)
            return ''.join(s_list)
        def getDown(s, pos):
            s_list = list(s)
            if s_list[pos] == '0':
                s_list[pos] = '9'
            else:
                s_list[pos] = str(int(s_list[pos]) - 1)
            return ''.join(s_list)
        
        q = deque()
        q.append('0000')
        visited = {'0000':1}
        deadends_dict = {s: 1 for s in deadends}
        depth = -1
        
        while(len(q) != 0):
            size = len(q)
            depth += 1
            for _ in range(size):
                cur = q.popleft()
                # check whether it is the target of one of the deadends
                if cur in deadends_dict:
                    continue
                if cur == target:
                    return depth
                visited[cur] = 1
                # visit all the neighbors
                for i in range(4):
                    neighbor = getUp(cur, i)
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited[neighbor] = 1
                    neighbor = getDown(cur, i)
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited[neighbor] = 1
        return -1