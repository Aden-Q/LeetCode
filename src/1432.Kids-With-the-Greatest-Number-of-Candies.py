class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        return list(map(lambda x: x >= max_candy - extraCandies, candies))