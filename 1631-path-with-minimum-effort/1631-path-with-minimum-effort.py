class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        import heapq
        dis = []
        rows = len(heights)
        cols = len(heights[0])
        for i in range(rows):
            arr = [float("inf")]*cols
            dis.append(arr)
        pq = []
        dis[0][0] = 0
        heapq.heappush(pq,[0,0,0])
        ind = [(0,1),(0,-1),(1,0),(-1,0)]
        while pq:
            eff,row,col = heapq.heappop(pq)
            for k in range(4):
                i = ind[k][0]+row
                j = ind[k][1]+col
                if 0<=i<rows and 0<=j<cols:
                    effort = max(eff,abs(heights[row][col] - heights[i][j]))
                    if effort<dis[i][j]:
                        heapq.heappush(pq,[effort,i,j])
                        dis[i][j] = effort
        return dis[rows-1][cols-1]

        

        