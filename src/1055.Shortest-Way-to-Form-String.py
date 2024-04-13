from collections import defaultdict

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_set = set(source)
        target_set = set(target)
        for c in target_set:
            if c not in source_set:
                return -1
        
        ptr_source = 0
        ptr_target = 0
        cnt = 0
        
        while ptr_target < len(target):
            while ptr_source < len(source) and ptr_target < len(target):
                if source[ptr_source] == target[ptr_target]:
                    ptr_source += 1
                    ptr_target += 1
                else:
                    ptr_source += 1
            
            cnt += 1
            ptr_source = 0
        
        return cnt