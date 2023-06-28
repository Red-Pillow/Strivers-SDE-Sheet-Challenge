# prob_link: https://www.codingninjas.com/studio/problems/clone-graph_8230812?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

# Class for graph node is as follows:
class graphNode:
    def __init__(self, *args):
        if(len(args) == 0):
            self.data = 0
            self.neighbours = []

        elif(len(args) == 1):
            self.data = args[0]
            self.neighbours = []

        elif(len(args) == 2):
            self.data = args[0]
            self.neighbours = args[1]

    def __del__(self):
        self.neighbours.clear()


def cloneGraph(node):
    from collections import deque, defaultdict
    # Write your code here.
    if not node:
        return node
    q=deque()
    q.append(node)
    visited=defaultdict(lambda:False)
    visited[node]=True
    dic={node: graphNode(node.data,[])}
    while len(q):
        n=q.popleft()
        for v in n.neighbours:
            if not visited[v]:
                q.append(v)
                visited[v]=True
                copy= graphNode(v.data,[])
                dic[v] =copy
            dic[n].neighbours.append(dic[v])
    return dic[node]
