# prob_link: https://www.codingninjas.com/studio/problems/longest-increasing-subsequence_8230689?challengeSlug=striver-sde-challenge&leftPanelTab=0

from sys import stdin
import sys

sys.setrecursionlimit(10 ** 7)


def longestIncreasingSubsequence(nums, n):
    # Your code goes here
    stack = []
    from bisect import bisect_left
    for i in range(len(nums)):
        if not stack:
            stack.append(nums[i])
            continue
        if nums[i] > stack[-1]:
            stack.append(nums[i])
        else:
            pos = bisect_left(stack, nums[i])
            stack[pos] = nums[i]

    return len(stack)


# taking inpit using fast I/O
def takeInput():
    n = int(input())

    if n == 0:
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


# main
arr, n = takeInput()
print(longestIncreasingSubsequence(arr, n))