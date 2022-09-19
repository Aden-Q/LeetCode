class Solution:
    def mySqrt(self, x: int) -> int:
        # Let x = k
        # y = x^2 - k 找右边的原点
        # 在点 (a, a^2 - k)处的切线斜率为2a
        # 该点的切线方程为y = 2ax - a^2 - k
        # 该切线与x轴的交点为 x = (a^2 + k) / (2a)
        # 迭代初始值可以为x
        if x < 2:
            return x
        
        x0 = x
        x1 = (x0 ** 2 + x) / (2 * x0)
        
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 ** 2 + x) / (2 * x0)
            
        return int(x1)