# prob link: https://www.codingninjas.com/codestudio/problems/next-permutation_8230741?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

def nextPermutation(nums, n):
    # Write your code here.
    # Return a list.
    mums = []
    for i in range(len(nums)):
        mums.append(nums[i])
    mums.sort(reverse=True)

    if mums == nums:
        mums.sort()
        for i in range(len(nums)):
            nums[i] = mums[i]
        return nums

    pos = -1
    stack = [nums[len(nums) - 1]]
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            stack.append(nums[i])
            pos = i
            break
        stack.append(nums[i])

    stack.sort()
    last_pos = -1
    for i in range(len(stack)):
        if stack[i] > nums[pos]:
            last_pos = i
            break

    if last_pos != -1:
        on_point = stack[last_pos]
        x = stack[:last_pos] + stack[last_pos + 1:]
        x.sort()

    ans = nums[:pos] + [on_point] + x
    for i in range(len(nums)):
        nums[i] = ans[i]
    return nums