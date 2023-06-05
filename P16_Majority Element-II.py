# prob_link: https://www.codingninjas.com/codestudio/problems/majority-element-ii_8230738?challengeSlug=striver-sde-challenge&leftPanelTab=0
from math import *
from collections import *
from sys import *
from os import *


def majorityElementII(arr):
    n = len(arr)
    # Write your code here.
    mp = {}
    for x in arr:
        if x not in mp:
            mp[x] = 1
        else:
            mp[x] += 1
    ans = []
    for key, val in mp.items():
        if val > floor(n / 3):
            ans.append(key)
    return ans
