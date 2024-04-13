class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        ans = 0
        for idx, ticket in enumerate(tickets):
            if ticket < tickets[k]:
                ans += ticket
            elif idx <= k:
                ans += tickets[k]
            else:
                ans += tickets[k] - 1

        return ans
