class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_damage = max(damage)
        if max_damage > armor:
            return sum(damage) - armor + 1
        else:
            return sum(damage) - max_damage + 1