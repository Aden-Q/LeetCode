class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_list = list(str(n))
        n_list = [int(i) for i in n_list]
        prod = 1
        sum_total = 0
        for num in n_list:
            sum_total += num
            prod *= num
        return prod - sum_total