# Prob_link: https://www.codingninjas.com/studio/problems/topological-sort_8230784?challengeSlug=striver-sde-challenge&leftPanelTab=1

from os import *
from sys import *
from collections import *
from math import *


def dfs(node, graph, visited, stack):
    # Append child before parent for all vertices
    visited[node] = True
    for adjNode in graph[node]:
        if not visited[adjNode]:
            dfs(adjNode, graph, visited, stack)
    stack.append(node)


def bfs(graph, in_degree, v):
    queue = deque()

    # Enqueue all vertices with in-degree 0
    for i in range(v):
        if in_degree[i] == 0:
            queue.append(i)

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        # Decrease the in-degree of adjacent vertices
        # and enqueue them if their in-degree becomes 0
        for adjNode in graph[node]:
            in_degree[adjNode] -= 1
            if in_degree[adjNode] == 0:
                queue.append(adjNode)

    return result


def topologicalSort(adj, v, e):
    # create adjacency list from edges pair
    graph = [[] for _ in range(v)]
    in_degree = [0] * v  # Store the in-degree of each vertex
    for i in range(e):
        u, v = adj[i]
        graph[u].append(v)
        in_degree[v] += 1

    # coz passed v is incorrect
    v = len(graph)

    visited = [False] * v
    stack = []

    # DFS approach
    for i in range(v):
        if not visited[i]:
            dfs(i, graph, visited, stack)

    # Reverse stack to make parents 1st and child later
    res = stack[::-1]

    # BFS or Kahn's algo
    res = bfs(graph, in_degree, v)

    return res