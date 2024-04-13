import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # Because the receptors are on the corner of the room
        # Horizontal speed is p, vertical speed is q
        # Horizontally we must make integer steps in order to reach a receptor
        # Vertically we must also make integer steps in order to reach a receptor
        # We have steps = lcm(p, q)
        k = p / gcd(p, q)
        
        if k % 2 == 0:
            return 2
        if (k * q // p) % 2 == 0:
            return 0
        return 1