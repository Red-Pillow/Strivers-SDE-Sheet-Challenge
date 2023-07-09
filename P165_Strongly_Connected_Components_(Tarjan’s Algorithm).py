# Prob_link: https://www.codingninjas.com/studio/problems/strongly-connected-components-tarjan-s-algorithm_8230789?challengeSlug=striver-sde-challenge&leftPanelTab=0

# This marks the discovery time of the nodes

discoveryTime = 1


def dfs(graph, node, disc, low, inStack, nodeStack, ans):
    global discoveryTime

    disc[node] = discoveryTime

    low[node] = discoveryTime

    discoveryTime += 1

    nodeStack.append(node)

    inStack[node] = True

    # Using Tarjan's algorithm here

    for v in graph[node]:

        # Looking into all unvisited nodes

        if disc[v] == -1:

            dfs(graph, v, disc, low, inStack, nodeStack, ans)

            low[node] = min(low[node], low[v])

        elif inStack[v]:

            low[node] = min(low[node], disc[v])

    # If current node is root of a SCC

    if low[node] == disc[node]:

        component = []

        # u marks the top element in the stack

        u = 0

        while nodeStack[-1] != node:
            u = nodeStack[-1]

            del nodeStack[-1]

            inStack[u] = False

            component.append(u)

        u = nodeStack[-1]

        del nodeStack[-1]

        inStack[u] = False

        component.append(u)

        ans.append(component)


def stronglyConnectedComponents(n, edges):
    # This stores our graph as Adjacency list

    graph = [[] for i in range(n)]

    for edge in edges:
        graph[edge[0]].append(edge[1])

    # Arrays to store the low-link value and discovery time of the nodes

    disc = [-1] * n

    low = [-1] * n

    nodeStack = []

    inStack = [False] * n

    ans = []

    for i in range(n):

        if disc[i] == -1:
            # Node i has not been visited yet

            dfs(graph, i, disc, low, inStack, nodeStack, ans)

    return ans
