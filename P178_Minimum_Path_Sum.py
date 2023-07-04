# prob_link: https://www.codingninjas.com/studio/problems/minimum-path-sum_8230791?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

import sys
sys.setrecursionlimit(10**7)

def minSumPath(grid):
    # Write your code here.
    n = len(grid)
    m = len(grid[0])
    def recur(i,j):
        if i<0 or j<0:
            return 1000000000000
        if i==0 and j==0:
            return grid[i][j]
        if (i,j) in dp:
            return dp[(i,j)]
        up = grid[i][j]+recur(i-1,j)
        left = grid[i][j]+recur(i,j-1)
        dp[(i,j)] = min(up,left)
        return dp[(i,j)]
    dp = {}
    return recur(n-1,m-1)

# Main.
t = int(input())
while (t > 0):
    l = list(map(int, input().split()))
    n,m = l[0], l[1]
    grid = []
    for i in range(n):
        ll = list(map(int, input().split()))
        grid.append(ll)
    print(minSumPath(grid))
    t -= 1