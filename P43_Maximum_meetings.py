# Prob_link: https://www.codingninjas.com/codestudio/problems/maximum-meetings_8230795?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *


def maximumMeetings(start, end):
    # Write your Code here.
    pair = []
    for i in range(len(start)):
        pair.append([start[i], end[i], i + 1])
    pair.sort(key=lambda x: x[1])
    stack = []
    for i in range(len(pair)):
        if not stack:
            stack.append(pair[i])
            continue
        if stack[-1][1] < pair[i][0]:
            stack.append(pair[i])

    ans = []
    for x, y, r in stack:
        ans.append(r)
    return ans


