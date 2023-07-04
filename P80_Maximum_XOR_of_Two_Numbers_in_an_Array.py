# prob_link: https://www.codingninjas.com/studio/problems/maximum-xor-of-two-numbers-in-an-array_8230852?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

from typing import *

def maximumXor(nums: List[int]) -> int:
    # Write your code here.
    arr=nums
    maxx = 0
    n=len(arr)
    mask = 0;
    se = set()
    for i in range(30, -1, -1):
        mask |= (1 << i)
        newMaxx = maxx | (1 << i)
        for i in range(n):
            se.add(arr[i] & mask)
        for prefix in se:
            if (newMaxx ^ prefix) in se:
                maxx = newMaxx
                break
        se.clear()
    return maxx