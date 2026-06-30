class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        dis = []
        for i in grid:
            arr = [float("inf")]*n
            dis.append(arr)
        dis[0][0] = 1
        q = deque()
        q.append([0,0])
        row = [1,-1,0,0,1,1,-1,-1]
        col = [0,0,1,-1,1,-1,-1,1]
        while q:
            curr = q.popleft()
            for k in range(len(row)):
                i = curr[0]+row[k]
                j = curr[1] + col[k]
                if i == n-1 and j == n-1:
                    return dis[curr[0]][curr[1]]+1
                elif 0<=i<n and 0<=j<n and dis[curr[0]][curr[1]]+1<dis[i][j] and grid[i][j] == 0:
                    q.append([i,j])
                    dis[i][j] = dis[curr[0]][curr[1]]+1
        if dis[n-1][n-1] == float("inf"):
            return -1
        return dis[n-1][n-1]



            
        