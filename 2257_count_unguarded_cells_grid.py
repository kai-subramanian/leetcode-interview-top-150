# You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.
# A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.
# Return the number of unoccupied cells that are not guarded.

def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        matrix=[[0 for i in range(n)] for i in range(m)]
        for r,c in guards:
            matrix[r][c]=1
        for r,c in walls:
            matrix[r][c]=1
        directions=[(-1,0),(1,0),(0,-1),(0,1)] #left,right, down and up.

        for r,c in guards:
            for dr, dc in directions:
                nr, nc=r+dr, c+dc
                while 0<=nr<m and 0<=nc<n:
                    if(matrix[nr][nc]==0):
                        matrix[nr][nc]=2 #guarded.
                    if(matrix[nr][nc]==1):
                        break
                    nr+=dr
                    nc+=dc
        ans=0
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==0):
                    ans+=1
        return ans