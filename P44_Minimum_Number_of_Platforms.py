# Prob_link: https://www.codingninjas.com/codestudio/problems/minimum-number-of-platforms_8230720?challengeSlug=striver-sde-challenge&leftPanelTab=0

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)


def calculateMinPatforms(at, dt, n):
    # Write your code here.
    maxdt = max(dt)
    aux = [0] * (maxdt + 2)
    for i in range(len(at)):
        aux[at[i]] += 1
        aux[dt[i] + 1] -= 1

    count = 0
    maxi = 0
    for i in range(len(aux)):
        count += aux[i]
        maxi = max(maxi, count)
    return maxi


