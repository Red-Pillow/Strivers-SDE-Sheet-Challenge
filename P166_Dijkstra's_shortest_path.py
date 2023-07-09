# Prob_link: https://www.codingninjas.com/studio/problems/dijkstra-s-shortest-path_8230755?challengeSlug=striver-sde-challenge&leftPanelTab=0

import heapq


def dijkstra(vec, vertices, edges, source):
    # Create adjacency list
    adj = [[] for _ in range(vertices)]
    for i, j, w in vec:
        adj[i].append((j, w))
        adj[j].append((i, w))

    dist = [2147483647] * vertices
    parent = [i for i in range(vertices)]
    pq = []  # Min heap

    heapq.heappush(pq, (0, source))
    dist[source] = 0

    while pq:
        dis, node = heapq.heappop(pq)

        for adjNode, eW in adj[node]:
            if dis + eW < dist[adjNode]:
                dist[adjNode] = dis + eW
                parent[adjNode] = node
                heapq.heappush(pq, (dist[adjNode], adjNode))

    return dist