class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows={}

        for row in grid:
            row=tuple(row)

            if row in rows:
                rows[row]+=1
            else:
                rows[row]=1
        count=0
        n=len(grid)

        for col in range(n):
            column=[]

            for row in range(n):
                column.append(grid[row][col])
            column=tuple(column)

            if column in rows:
                count+=rows[column]
        return count



        