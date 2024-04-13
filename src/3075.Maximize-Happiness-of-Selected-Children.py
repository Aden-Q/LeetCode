class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        total_happiness = 0
        for turn in range(k):
            if not happiness:
                break
            # select the last person
            last_num = happiness.pop()
            if last_num > turn:
                total_happiness += last_num - turn
            else:
                return total_happiness
                
        return total_happiness
