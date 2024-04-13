class UnionFind:
    def __init__(self):
        self.parent = defaultdict(int)
        self.num_components = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return

        self.parent[root_x] = root_y
        self.num_components -= 1
        
        return

    def add(self, x):
        self.parent[x] = x
        self.num_components += 1
        
        return

    def exist(self, x):
        return x in self.parent

    def getNumComponnts(self):
        return self.num_components


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        nums = set(nums)

        # prime factors + union & find
        def factorization(num) -> List[int]:
            res = []
            
            n = 2
            while n * n <= num:
                if num % n == 0:
                    res.append(n)
                    while num % n == 0:
                        num //= n
                
                n += 1

            if num > 1:
                res.append(num)

            return res

        uf = UnionFind()
        for num in nums:
            prime_factors = factorization(num)
            if len(prime_factors) == 0:
                # if it's a prime, then immediately return false
                return False
            # otherwise we union all those prime factors
            for i in range(len(prime_factors)):
                if not uf.exist(prime_factors[i]):
                    uf.add(prime_factors[i])
                uf.union(prime_factors[0], prime_factors[i])

        return uf.getNumComponnts() == 1
