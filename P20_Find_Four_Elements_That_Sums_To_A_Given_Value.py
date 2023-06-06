# Prob_link: https://www.codingninjas.com/codestudio/problems/find-four-elements-that-sums-to-a-given-value_8230785?challengeSlug=striver-sde-challenge&leftPanelTab=0

from math import *
from collections import *
from sys import *
from os import *


def fourSum(nums, target):
    N = len(nums)
    aux1 = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            aux1.append([nums[i] + nums[j], i, j])
    flag = False
    for i in range(len(aux1) - 1):
        for j in range(i + 1, len(aux1)):
            v1 = aux1[i][0]
            a = aux1[i][1]
            b = aux1[i][2]

            v2 = aux1[j][0]
            c = aux1[j][1]
            d = aux1[j][2]
            if v1 + v2 == target and a < b < c < d:
                return "Yes"
    return "No"
