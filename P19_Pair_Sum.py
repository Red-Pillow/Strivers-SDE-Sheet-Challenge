# Prob_link: https://www.codingninjas.com/codestudio/problems/pair-sum_8230699?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *


def pairSum(nums, s):
    # Write your code here.
    nums.sort()
    mp = {}
    for i in range(len(nums)):
        if nums[i] not in mp:
            mp[nums[i]] = 1
        else:
            mp[nums[i]] += 1

    seen = set()
    ans = []
    for i in range(len(nums)):

        if (s - nums[i]) in mp and ((nums[i], s - nums[i]) not in seen or (s - nums[i], nums[i]) not in seen):
            freq1 = mp[s - nums[i]]
            freq2 = mp[nums[i]]
            total_pairs = freq1 * freq2
            val1 = nums[i]
            val2 = s - nums[i]
            if s - nums[i] == nums[i]:
                if mp[nums[i]] == 1:
                    seen.add((nums[i], s - nums[i]))
                    seen.add((s - nums[i], nums[i]))
                    break

                total_pairs = freq1 * (freq1 - 1) // 2

            for j in range(total_pairs):
                ans.append([val1, val2])
            seen.add((nums[i], s - nums[i]))
            seen.add((s - nums[i], nums[i]))

    for i in range(len(ans)):
        ans[i] = sorted(ans[i])
    ans.sort()

    return ans    
