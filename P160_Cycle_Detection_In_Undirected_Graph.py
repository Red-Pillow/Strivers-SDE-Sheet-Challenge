# Prob_link: https://www.codingninjas.com/studio/problems/cycle-detection-in-undirected-graph_8230798?challengeSlug=striver-sde-challenge&leftPanelTab=0

from collections import deque
def getAdjList(edges, n):
    adjList = [[] for i in range(0, n+1)]
    for v1, v2 in edges:
        if v1 not in adjList[v2]:
            adjList[v2].append(v1)
        if v2 not in adjList[v1]:
            adjList[v1].append(v2)
    return adjList
def isCycle(i, n, adjList, visited):
    q = deque([(i, -1)])
    visited[i] = 1
    #print("queue and visited", q, visited)
    while q:
        node, parent = q.popleft()
        #print("node and parent: ", node, parent)
        for des in adjList[node]:
            #print("descendant and adj[node]", des, adjList[node])
            if not visited[des]:
                visited[des] = 1
                q.append((des, node))
                #print("not visited descendant", des, q)
            else:
                if parent!=des:
                    #print("parent and des are different", parent, des)
                    return True
    return False
def cycleDetection(edges, n, m):
    # Write your code here.
    # Return "Yes" if cycle id present in the graph else return "No".
    adjList = getAdjList(edges, n)
    #print("adjList", adjList)
    visited = [0]*(n+1)
    #print("initial visited", visited)
    for i in range(1, n+1):
        if not visited[i]:
            #print("initial not visited i ", i)
            if isCycle(i, n, adjList, visited):
                return "Yes"
    return "No"