# prob_link: https://www.codingninjas.com/codestudio/problems/longest-consecutive-sequence_8230708?challengeSlug=striver-sde-challenge&leftPanelTab=0

from math import *
from collections import *
from sys import *
from os import *


def lengthOfLongestConsecutiveSequence(nums, n):
    # Write your code here.
    seen = set()
    for x in nums:
        seen.add(x)
    nums = list(set(nums))
    maxi = 0
    head = []
    for i in range(len(nums)):
        if nums[i] - 1 not in seen:
            head.append(nums[i])

    for x in head:
        c = 0
        value = x
        while (value in seen):
            c += 1
            value += 1
        maxi = max(maxi, c)
    return maxi

