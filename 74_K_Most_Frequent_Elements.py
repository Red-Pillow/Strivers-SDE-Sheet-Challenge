# prob_link: https://www.codingninjas.com/studio/problems/k-most-frequent-elements_8230853?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

from typing import List


def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:
    # write your code here
    mp = {}
    for i in range(len(arr)):
        if arr[i] not in mp:
            mp[arr[i]] = 1
        else:
            mp[arr[i]] += 1

    pair = []
    for key,val in mp.items():
        pair.append([key,val])
    ans = []
    pair.sort(key=lambda x:x[1], reverse = True)
    pair = pair[:k]
    for key,val in pair:
        ans.append(key)
    ans.sort()
    return ans