class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        total = sum(skill)
        if total % (n // 2) != 0:
            return -1

        totalSkillEachGroup = total // (n // 2)
        chemistry = 0
        counter = Counter(skill)
        
        for s in skill:
            if not counter[s]:
                continue
            counter[s] -= 1
            if not counter[totalSkillEachGroup - s]:
                # no pair can be found
                return -1
            counter[totalSkillEachGroup - s] -= 1
            chemistry += s * (totalSkillEachGroup - s)
        
        return chemistry
