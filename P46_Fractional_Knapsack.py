# Prob_link: https://www.codingninjas.com/studio/problems/fractional-knapsack_8230767?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *


def maximumValue(items, n, w):
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    value = 0
    for item in items:
        if item[0] <= w:
            w -= item[0]
            value += item[1]
        elif item[0] > w:
            value += (item[1] / item[0]) * w
            w = 0
            break
    return value