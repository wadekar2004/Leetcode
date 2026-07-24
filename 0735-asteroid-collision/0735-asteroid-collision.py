class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack=[]

        for aster in asteroids:
            alive=True

            while alive and stack and stack[-1] > 0 and aster < 0:
                if stack[-1]<abs(aster):
                    stack.pop()

                elif stack[-1]==abs(aster):
                    stack.pop()
                    alive=False
                else:
                    alive= False
            if alive:
                stack.append(aster)
        return stack


        