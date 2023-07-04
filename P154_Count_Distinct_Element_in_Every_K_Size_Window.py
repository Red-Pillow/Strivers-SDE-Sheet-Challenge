# prob_link: https://www.codingninjas.com/studio/problems/count-distinct-element-in-every-k-size-window_8230749?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *


def countDistinctElements(nums, k):
    # Write your code here
    mp = {}
    left = 0

    mp = {}
    ans = []
    for i in range(k):
        if nums[i] not in mp:
            mp[nums[i]] = 1
        else:
            mp[nums[i]] += 1

    ans.append(len(mp))
    for right in range(k, len(nums)):
        if nums[right] not in mp:
            mp[nums[right]] = 1
        else:
            mp[nums[right]] += 1

        while (right - left >= k):
            if nums[left] in mp:
                mp[nums[left]] -= 1
                if mp[nums[left]] == 0:
                    del mp[nums[left]]
            left += 1

        if right - left + 1 == k:
            ans.append(len(mp))
    return ans
