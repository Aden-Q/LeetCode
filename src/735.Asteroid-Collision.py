class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # O(N) time and O(N) space
        # It can be implemented with a straightforward simulation with stack
        stack = []
        for asteroid in asteroids:
            currExploded = False
            
            while stack and asteroid < 0 and stack[-1] > 0:
                # collision happens
                if abs(asteroid) < abs(stack[-1]):
                    # The current asteroid exploded and no more explore is needed
                    currExploded = True
                    break
                elif abs(asteroid) == abs(stack[-1]):
                    # Both exploded
                    currExploded = True
                    stack.pop()
                    break
                else:
                    # Further checks are needed
                    stack.pop()
                
            if not currExploded:
                stack.append(asteroid)
        
        return stack