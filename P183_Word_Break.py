# prob_link: https://www.codingninjas.com/studio/problems/word-break_8230808?challengeSlug=striver-sde-challenge&leftPanelTab=0


from os import *
from sys import *
from collections import *
from math import *


def wordBreak(wordDict, n, s):
    # Write your code here.
    n = len(s)
    st = set(wordDict)
    mp = {}

    def recur(index):
        if index == n:
            return True
        if index in mp:
            return mp[index]
        sub = ""
        for i in range(index, n):
            sub += s[i]
            if sub in st and recur(i + 1) == True:
                mp[index] = True
                return mp[index]

        mp[index] = False
        return mp[index]

    return recur(0)