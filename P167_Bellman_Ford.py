# Prob_link: https://www.codingninjas.com/studio/problems/bellman-ford_8230845?challengeSlug=striver-sde-challenge&leftPanelTab=0

def bellmonFord(n, m, src, dest, edges):
    dist = [1e9]*(n+1)
    dist[src] = 0
    for i in range(n):
        for u,v,w in edges:
            if dist[u]+w < dist[v]:
                dist[v] = dist[u]+w

    return dist[dest] if dist[dest] < 1e8 else int(1e9)