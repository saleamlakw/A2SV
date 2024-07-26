class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[math.inf] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        cnt = [0] * n
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if dist[i][j] <= distanceThreshold:
                    cnt[j] += 1

        ans = 0
        for i in range(n):
            if cnt[i] <= cnt[ans]:
                ans = i
        return ans