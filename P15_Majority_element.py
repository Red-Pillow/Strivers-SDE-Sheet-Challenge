# prob_link: https://www.codingninjas.com/codestudio/problems/day-6-majority-element_8230731?challengeSlug=striver-sde-challenge&leftPanelTab=0


from math import *
from collections import *
from sys import *
from os import *


def findMajorityElement(arr, n):
    # Write your code here.

    n = len(arr)
    mp = {}
    for x in arr:
        if x not in mp:
            mp[x] = 1
        else:
            mp[x] += 1

    for key, val in mp.items():
        if val > floor(n / 2):
            return key

    return -1
