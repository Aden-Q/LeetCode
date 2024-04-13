class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        n = len(inventory)
        inventory.sort(reverse=True)
        mod = 10 ** 9 + 7
        
        # we need to find the maxmize k such the number of products sold with price >= k is >= orders
        def feasible(k) -> bool:
            total = 0
            for val in inventory:
                if val < k:
                    continue
                total += val - k + 1
                if total >= orders:
                    return True

            return False

        left, right = 0, max(inventory) + 1
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                left = mid + 1
            else:
                right = mid

        # ok now right - 1 is the number we need to find
        k = left - 1
        # we need to calculate the total gain
        total = 0
        for idx, val in enumerate(inventory):
            if val < k:
                continue
                
            amount_to_sell = min(orders, val - k)
            curr_val = ((val + val - amount_to_sell + 1) * amount_to_sell) // 2
            total = (total + curr_val % mod) % mod
            orders -= amount_to_sell
            inventory[idx] -= amount_to_sell

            if orders == 0:
                break

        if orders > 0:
            total = (total + k * orders % mod) % mod

        return total
