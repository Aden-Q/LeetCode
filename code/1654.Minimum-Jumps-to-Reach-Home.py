class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        self.res = -1
        
        def dfs(cur_x, cnt, back):
            # back = False if forward (previous step)
            # back = True if backward (previous step)
            # print(cur_x, ' ', cnt)
            if self.res < 0 and cur_x <= 6000:
                if cur_x == x:
                    self.res = cnt
                    return
                if cur_x + a not in forbidden:
                    forbidden.add(cur_x + a)
                    dfs(cur_x+a, cnt+1, False)
                if not back and cur_x - b >= 0 and cur_x - b not in forbidden:
                    dfs(cur_x-b, cnt+1, True)
            
        dfs(0, 0, False)
        return self.res
        