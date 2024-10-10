class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        def build_graph(n, edges, probability):
            graph = {}
            for i in range(n):
                graph[i] = []
            for i in range(len(edges)):
                frm, to = edges[i]
                graph[frm].append((probability[i], to))
                graph[to].append((probability[i], frm))
            return graph
        def bfs(graph):
            import heapq as hq
            dist = {start:-1}
            heap = [(-1, start)]
            hq.heapify(heap)
            while len(heap) > 0:
                prob, node = hq.heappop(heap)
                for child in graph[node]:
                    p,c = child
                    if c in dist:
                        if abs(p*prob) > abs(dist[c]):
                            hq.heappush(heap, (-abs(p*prob), c))
                            dist[c] = -abs(p*prob)
                    else:
                        hq.heappush(heap, (-abs(p * prob), c))
                        dist[c] = -abs(p * prob)
            return 0 if end not in dist else -dist[end]

        return bfs(build_graph(n, edges, succProb))