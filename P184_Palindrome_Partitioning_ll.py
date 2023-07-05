# prob_link: https://www.codingninjas.com/studio/problems/palindrome-partitioning-ll_8230732?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
import sys

setrecursionlimit(10 ** 6)


def palindromePartitioning(s):
    # Write your code here.
    dp = [[-1 for i in range(len(s))] for i in range(len(s))]

    def isPalindrome(s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i = i + 1
            j = j - 1
        return True

    def sol(s, i, j):
        if i == j or isPalindrome(s, i, j):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        minn = float('inf')

        for k in range(i, j):
            if dp[i][k] != -1:
                left = dp[i][k]
            else:
                left = sol(s, i, k)
                dp[i][k] = left
            if dp[k + 1][j] != -1:
                right = dp[k + 1][j]
            else:
                right = sol(s, k + 1, j)
                dp[k + 1][j] = right
            count = 1 + left + right

            if count < minn:
                minn = count
        dp[i][j] = minn
        return dp[i][j]

    return sol(s, 0, len(s) - 1)


# Main
t = int(input())
while t:
    string = list(map(str, input()))
    while (" " in string):
        string.remove(" ")
    print(palindromePartitioning(string))
    t = t - 1
