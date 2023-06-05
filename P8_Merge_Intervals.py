# prob_link: https://www.codingninjas.com/codestudio/problems/merge-intervals_8230700?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit


class Solution:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def mergeIntervals(intervals):
    # Write your code here.
    intervals.sort(key=lambda x: x.start)
    stack = []
    for x in intervals:
        if not stack or x.start > stack[-1].end:
            stack.append(x)
        else:
            stack[-1].end = max(stack[-1].end, x.end)
    return stack


n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    intervals.append(a)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start, res[i].end)

