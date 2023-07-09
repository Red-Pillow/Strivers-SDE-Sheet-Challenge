# Prob_link: https://www.codingninjas.com/studio/problems/lru-cache-implementation_8230697?challengeSlug=striver-sde-challenge&leftPanelTab=0


from sys import stdin
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = OrderedDict()

    def get(self, key):
        if key not in self.values:
            return -1
        else:
            self.values[key] = self.values.pop(key)
            return self.values[key]

    def put(self, key, value):
        if key not in self.values:
            if len(self.values) == self.capacity:
                self.values.popitem(last=False)
        else:
            self.values.pop(key)
        self.values[key] = value


# main
capacity, q = map(int, stdin.readline().rstrip().split(" "))

cache = LRUCache(capacity)

while q != 0:
    query = list(map(int, stdin.readline().rstrip().split()))

    if query[0] == 0:
        key = query[1]
        print(cache.get(key))
    elif query[0] == 1:
        key = query[1]
        value = query[2]
        cache.put(key, value)

    q -= 1