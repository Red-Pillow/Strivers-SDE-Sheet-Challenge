# prob_link: https://www.codingninjas.com/codestudio/problems/subsets-ii_8230855?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

from typing import *


def uniqueSubsets(n: int, nums: List[int]) -> List[List[int]]:
    # Write your code here.
    N = len(nums)

    def recur(index, nums, ds):
        ans.append(ds[:])

        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue

            ds.append(nums[i])
            recur(i + 1, nums, ds)
            ds.pop()

    ans = []
    nums.sort()
    recur(0, nums, [])
    return ans[1:]

