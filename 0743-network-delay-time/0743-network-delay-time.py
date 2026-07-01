class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        import heapq
        dis = [float("inf")]*(n+1)
        dis[k] = 0
        dis[0] = 0
        adj=[]
        for i in range(n+1):
            adj.append([])
        for src,dst,time in times:
            adj[src].append([dst,time])
        q = []
        heapq.heappush(q,[0,k])
        while q:
            time,dst = heapq.heappop(q)
            for i,j in adj[dst]:
                if time+j<dis[i]:
                    dis[i] = time+j
                    heapq.heappush(q,[time+j,i])
        maxi = max(dis)
        if maxi == float("inf"):
            return -1
        return maxi



        