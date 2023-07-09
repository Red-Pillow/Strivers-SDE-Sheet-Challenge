# Prob_link: https://www.codingninjas.com/studio/problems/complete-string_8230849?challengeSlug=striver-sde-challenge&leftPanelTab=0



class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        curr = self.root
        for ch in string:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True

    def allPrefixExists(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
            if not curr.isEnd:
                return False
        return True


def completeString(n, a):
    trie = Trie()
    for word in a:
        trie.insert(word)

    res = ''
    for word in a:
        if trie.allPrefixExists(word):
            if len(word) == len(res):
                res = min(res, word)
            elif len(word) > len(res):
                res = word

    return res if len(res) > 0 else None