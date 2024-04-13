class ProductOfNumbers:

    # O(n) space with the usage of a queue/array data structure
    def __init__(self):
        self.q = []
        # prefixProd[i+1] = prod(q[0], q[1], ..., q[i])
        self.prefixProd = [1]
        self.zerosIndex = []
    
    # O(1) time
    def add(self, num: int) -> None:
        self.q.append(num)
        if num == 0:
            self.zerosIndex.append(len(self.q) - 1)
            self.prefixProd.append(self.prefixProd[-1])
        else:
            self.prefixProd.append(self.prefixProd[-1] * num)
        
    # O(1) query for production
    def getProduct(self, k: int) -> int:
        # We want to calculate self.q[-1] * self.q[-2] * ... * self.q[-k]
        # self.q[-k] = self.[n-k]
        if self.zerosIndex and self.zerosIndex[-1] >= len(self.q) - k:
            return 0
        return self.prefixProd[-1] // self.prefixProd[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)