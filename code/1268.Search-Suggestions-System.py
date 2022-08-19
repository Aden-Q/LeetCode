class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        start = 0
        
        for i in range(len(searchWord)):
            prefix = searchWord[:i+1]
            cur_res = []
            idx = bisect.bisect_left(products, prefix, lo = start)
            if idx < len(products) and prefix == products[idx][:i+1]:
                cur_res.append(products[idx])
            if idx + 1 < len(products) and prefix == products[idx+1][:i+1]:
                cur_res.append(products[idx+1])
            if idx + 2 < len(products) and prefix == products[idx+2][:i+1]:
                cur_res.append(products[idx+2])
            start = idx
            res.append(cur_res[:])
            
        return res