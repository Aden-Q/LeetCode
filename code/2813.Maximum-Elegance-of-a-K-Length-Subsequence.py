class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(reverse=True)
        categories_seen = set()
        duplicates = []
        curr = 0
        ans = -inf

        for price, category in items:
            curr += price
            if category not in categories_seen:
                categories_seen.add(category)
            else:
                duplicates.append(price)

            while duplicates and len(duplicates) + len(categories_seen) > k:
                curr -= duplicates.pop()
            
            if len(duplicates) + len(categories_seen) == k:
                ans = max(ans, curr + len(categories_seen) ** 2)

        return ans
