class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        ans = 0
        p_idx = 0
        t_idx = 0
        while p_idx < len(players) and t_idx < len(trainers):
            if players[p_idx] <= trainers[t_idx]:
                # yes, there's a match
                ans += 1
                # we cannot reuse a trainer
                p_idx += 1
                t_idx += 1
            else:
                # the current trainer cannot match the player which has the lowest ability so far
                t_idx += 1

        return ans