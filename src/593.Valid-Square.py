class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        v1 = (p2[0] - p1[0], p2[1] - p1[1])
        v2 = (p3[0] - p1[0], p3[1] - p1[1])
        v3 = (p4[0] - p1[0], p4[1] - p1[1])

        # calculatet the dot product of 2 vectors
        def dotProduct(v1, v2) -> int:
            return v1[0] * v2[0] + v1[1] * v2[1]

        def vecLength(v) -> int:
            return sqrt(v[0] ** 2 + v[1] ** 2)

        if dotProduct(v1, v3) != 0 and dotProduct(v1, v3) != 0:
            v1, v2, v3 = v2, v3, v1

        if dotProduct(v1, v2) != 0:
            v2, v3 = v3, v2

        if dotProduct(v1, v2) != 0:
            return False

        # now v3 is the diagnal
        if vecLength(v1) == 0:
            return False

        if abs(vecLength(v1) - vecLength(v2)) > 1e-6:
            return False

        if abs(vecLength(v3) - sqrt(2) * vecLength(v1)) > 1e-6:
            return False

        return dotProduct(v1, v3) == dotProduct(v2, v3)
