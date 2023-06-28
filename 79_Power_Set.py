# prob_link: https://www.codingninjas.com/studio/problems/power-set_8230797?challengeSlug=striver-sde-challenge&leftPanelTab=0


from os import *
from sys import *
from collections import *
from math import *


def pwset(v):
    # Write your code here
    # Return a 2-D list containing all subsets
    subsets = []

    def generateSubsets(index, nums, current, subsets):
        subsets.append(current[:])
        for i in range(index, len(nums)):
            current.append(nums[i])
            generateSubsets(i + 1, nums, current, subsets)
            current.remove(current[-1])

    generateSubsets(0, v, [], subsets)
    return subsets