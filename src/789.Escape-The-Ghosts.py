class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        # if any ghost is closer to the target than the player, then it's impossible
        targe_dist_from_player = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            if abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) <= targe_dist_from_player:
                return False
        
        return True
