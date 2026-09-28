from collections import deque

class Solution:
    def nearestExit(self, maze, entrance):

        q = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'

        while q:
            r, c, steps = q.popleft()

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
                    if maze[nr][nc] == '.':

                        maze[nr][nc] = '+'

                        if nr == 0 or nr == len(maze)-1 or nc == 0 or nc == len(maze[0])-1:
                            return steps + 1

                        q.append((nr, nc, steps + 1))

        return -1