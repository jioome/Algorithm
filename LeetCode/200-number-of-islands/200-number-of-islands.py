class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        output = 0 
        def dfs(grid,x,y) : 
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]
            grid[x][y] = "0"
            for i in range(4):
                nx= x + dx[i]
                ny = y + dy[i]
                if 0<= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "0":
                    dfs(grid,nx,ny)
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "0":
                    output += 1 
                    dfs(grid,i,j)
        return output