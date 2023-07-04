# prob_link: https://www.codingninjas.com/studio/problems/implement-trie_8230696?challengeSlug=striver-sde-challenge&leftPanelTab=0

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)


class TrieNode:
    def __init__(self):
        self.wordend = False
        self.alpha = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

        # constructor for the Trie

    def insert(self, word):
        n = len(word)
        r = self.root
        for w in word:
            if w not in r.alpha:
                r.alpha[w] = TrieNode()
            r = r.alpha[w]
        r.wordend = True

    def search(self, word):

        r = self.root
        for w in word:
            if not r:
                return False
            if w not in r.alpha:
                return False
            r = r.alpha[w]
        return r.wordend

    def startWith(self, prefix):
        r = self.root
        for w in prefix:
            if not r:
                return False
            if w not in r.alpha:
                return False
            r = r.alpha[w]
        return True


# main
t = int(input().strip())
root = Trie()
for i in range(t):

    q_str = stdin.readline().strip().split(" ")
    q = int(q_str[0].strip())
    str1 = q_str[1].strip()

    if (q == 1):
        root.insert(str1)

    elif (q == 2):
        if (root.search(str1)):
            print("true")

        else:
            print("false")

    else:
        if (root.startWith(str1)):
            print("true")

        else:
            print("false")

