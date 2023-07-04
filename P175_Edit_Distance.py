# prob_link: https://www.codingninjas.com/studio/problems/edit-distance_8230685?challengeSlug=striver-sde-challenge&leftPanelTab=0


from sys import stdin
import sys

sys.setrecursionlimit(10 ** 7)


def editDistance(word1, word2):
    # Your code goes here
    n = len(word1)
    m = len(word2)
    mp = {}

    def recur(n, m):
        if n == 0 and m == 0:
            return 0
        if n == 0:
            return m
        if m == 0:
            return n
        if (n, m) in mp:
            return mp[(n, m)]
        if word1[n - 1] == word2[m - 1]:
            mp[(n, m)] = recur(n - 1, m - 1)
            return mp[(n, m)]
        mp[(n, m)] = 1 + min(recur(n, m - 1), recur(n - 1, m), recur(n - 1, m - 1))
        return mp[(n, m)]

    return recur(n, m)


# taking inpit using fast I/O
def takeInput():
    str1 = input()
    str2 = input()

    return str1, str2


# main
str1, str2 = takeInput()
print(editDistance(str1, str2))
