class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size+1)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        
        # decompose a number into a set of prime factors
        def decompose(num) -> List[int]:
            prime_factors = set()
            factor = 2

            while num >= factor ** 2:
                if num % factor == 0:
                    prime_factors.add(factor)
                    num = num // factor
                else:
                    factor += 1

            prime_factors.add(num)
            return list(prime_factors)

        uf = UnionFind(max(nums))
        lookup_table = {}
        for num in nums:
            # every number must have at least one prime factor
            prime_factors = decompose(num)
            lookup_table[num] = prime_factors[0]
            for idx in range(len(prime_factors) - 1):
                uf.union(prime_factors[idx], prime_factors[idx+1])

        counter = Counter()
        for num in nums:
            counter[uf.find(lookup_table[num])] += 1

        return max(counter.values())
