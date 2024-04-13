from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # We need a map to mainting the name -> city of transaction -> min_time, max_time of transactions
        mp = defaultdict(defaultdict)
        res = []
        
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            time = int(time)
            amount = int(amount)
            if name not in mp or city not in mp[name]:
                mp[name][city] = [time]
            else:
                mp[name][city].append(time)
        
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            time = int(time)
            amount = int(amount)
            if amount > 1000:
                res.append(transaction)
            else:
                is_invalid = False
                for other_city in mp[name]:
                    if is_invalid:
                        break
                    if other_city == city:
                        continue
                    for other_time in mp[name][other_city]:
                        if other_time - 60 <= time and other_time + 60 >= time:
                            res.append(transaction)
                            is_invalid = True
                            break
        
        return res