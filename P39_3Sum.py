# prob_link: https://www.codingninjas.com/codestudio/problems/3sum_8230739?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit


def findTriplets(nums, n, k):
    # Write your code here.
    kk = k
    nums.sort()
    l = []
    for i in range(len(nums)):
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        j = i + 1
        k = len(nums) - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s > kk:
                k -= 1
            elif s < kk:
                j += 1
            else:
                l.append([nums[i], nums[j], nums[k]])
                j += 1
                while nums[j - 1] == nums[j] and j < k:
                    j += 1
    return l


# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    K = int(stdin.readline())
    return N, arr, K


tc = int(input())
while tc > 0:
    N, arr, K = takeInput()
    ans = findTriplets(arr, N, K)

    if len(ans) == 0:
        stdout.write("-1\n")

    else:
        for i in ans:
            i.sort()
            stdout.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")

    tc -= 1
