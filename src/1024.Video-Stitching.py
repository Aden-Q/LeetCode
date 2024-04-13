class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key = lambda x : (x[0], -x[1]))
        if clips[0][0] > 0:
            return -1
        cur_end = 0
        next_end = 0
        cnt = 0
        idx = 0
        while idx < len(clips) and clips[idx][0] <= cur_end:
            while idx < len(clips) and clips[idx][0] <= cur_end:
                next_end = max(next_end, clips[idx][1])
                idx += 1
            cnt += 1
            cur_end = next_end
            if cur_end >= time:
                return cnt
        
        return -1