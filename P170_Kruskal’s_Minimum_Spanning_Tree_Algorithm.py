# Prob_link: https://www.codingninjas.com/studio/problems/kruskal-s-minimum-spanning-tree-algorithm_8230804?challengeSlug=striver-sde-challenge&leftPanelTab=0

class Disjoint:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def findParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u, v):
        pu = self.findParent(u)
        pv = self.findParent(v)
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]


def kruskalMST(n, m, graph):
    edges = []
    for i in graph:
        u, v, wt = i[0], i[1], i[2]
        edges.append((wt, (u, v)))
        edges.append((wt, (v, u)))

    edges.sort()
    d = Disjoint(n)
    sum = 0

    for wt, (u, v) in edges:
        if d.findParent(u) != d.findParent(v):
            sum += wt
            d.unionBySize(u, v)

    return sum