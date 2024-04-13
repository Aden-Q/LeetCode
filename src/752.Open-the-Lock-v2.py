from collections import deque
from collections import Counter

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = Counter(deadends)
        if '0000' in deadends:
            return -1
        q = deque(['0000'])
        dc = {'0000': 1}
        choices = {'0': ['1', '9'],
                   '1': ['0', '2'],
                   '2': ['1', '3'],
                   '3': ['2', '4'],
                   '4': ['3', '5'],
                   '5': ['4', '6'],
                   '6': ['5', '7'],
                   '7': ['6', '8'],
                   '8': ['7', '9'],
                   '9': ['0', '8']}
        step = -1
        while len(q) != 0:
            sz = len(q)
            step += 1
            for _ in range(sz):
                cur_node = q.popleft()
                if cur_node == target:
                    return step
                for i in range(4):
                    for choice in choices[cur_node[i]]:
                        next_node = cur_node[:i] + choice + cur_node[i+1:]
                        if next_node not in deadends and next_node not in dc:
                            dc[next_node] = 1
                            q.append(next_node)
        return -1