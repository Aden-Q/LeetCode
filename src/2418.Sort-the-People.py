class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_indices = sorted(range(len(names)), key=lambda x: -heights[x])

        return [names[i] for i in sorted_indices]
