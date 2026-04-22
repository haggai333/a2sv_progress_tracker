class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            alive = True
            while alive and asteroid < 0 and stack and stack[-1] > 0:
                top = stack.pop()
                if abs(top) > abs(asteroid):
                    stack.append(top)
                    alive = False
                elif abs(top) == abs(asteroid):
                    alive = False
            if alive:
                stack.append(asteroid)
        
        return stack
