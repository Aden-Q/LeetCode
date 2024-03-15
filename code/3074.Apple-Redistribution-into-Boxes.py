class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        ans = 0
        total_apple = sum(apple)
        for cap in capacity:
            total_apple -= cap
            ans += 1
            if total_apple <= 0:
                break
                
        return ans
