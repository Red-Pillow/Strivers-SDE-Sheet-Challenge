# prob_link: https://www.codingninjas.com/studio/problems/maximum-sum-increasing-subsequence_8230821?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *
import sys


def maxIncreasingDumbbellsSum(rack, n):
    # Write your code here

    # base case: nothing is remaining
    def MSIS(nums, i=0, prev=-sys.maxsize, total=0):

        # base case: nothing is remaining
        if i == len(nums):
            return total

        if (i, total) in mp:
            return mp[(i, total)]
        # case 1: exclude the current element and process the
        # remaining elements
        excl = MSIS(nums, i + 1, prev, total)

        # case 2: include the current element if it is greater
        # than the previous element
        incl = total
        if nums[i] > prev:
            incl = MSIS(nums, i + 1, nums[i], total + nums[i])

        # return the maximum of the above two choices
        mp[(i, total)] = max(incl, excl)
        return mp[(i, total)]

    mp = {}
    return MSIS(rack)
