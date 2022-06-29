class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ## row and column number
        m, n = len(grid), len(grid[0])
		## Creating an empty set for keeping track of the visitied position
        visited = set() 
		## Directions in which we can move
        d = [(1,0),(0,1),(-1,0),(0,-1)]
        ans = 0
        def dfs(r, c):
			## adding the row and column number to the visited set
            visited.add((r,c))
            for dx, dy in d:
                r_x, c_y = r + dx, c + dy
				## if the position is already visited or has water ('0'), we skip
                if r_x < 0 or r_x >= m or c_y < 0 or c_y >= n or grid[r_x][c_y] == '0' or (r_x, c_y) in visited:
                    continue
				## if all the conditions are met, function is called recursively
                dfs(r_x, c_y)
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs(i, j)
					## when the dfs function completes, it means it has found an island
					## so we increase the answer
                    ans += 1
        return ans