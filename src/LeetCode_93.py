class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        path = []
        res = []
        size = len(s)
        def is_legal(s):
            if len(s) == 0:
                return False
            elif len(s) > 1 and s[0] == '0':
                return False
            elif int(s) > 255:
                return False
            else:
                return True
            
        def backtracking(s, start_idx, num_split):
            nonlocal path, res
            if num_split == 3:
                last_seg = s[start_idx:]
                if is_legal(last_seg):
                    path.append(last_seg)
                    res.append('.'.join(path[:]))
                    path.pop()
                return
            elif start_idx > size - 1:
                return
            for i in range(1, 4):
                if is_legal(s[start_idx:start_idx+i]):
                    # legal address
                    path.append(s[start_idx:start_idx+i])
                    backtracking(s, start_idx+i, num_split + 1)
                    path.pop()
                    
        backtracking(s, 0, 0)
        return res