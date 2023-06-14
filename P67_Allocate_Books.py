# prob_link: https://www.codingninjas.com/codestudio/problems/allocate-books_8230810?challengeSlug=striver-sde-challenge&leftPanelTab=0
from os import *
from sys import *
from collections import *
from math import *


def ayushGivesNinjatest(n, A, B):
    def check(mid):
        summ = 0
        count = 1
        for i in range(len(B)):
            if summ + B[i] > mid:
                summ = B[i]
                count += 1
            else:
                summ += B[i]
            if count > n or B[i] > mid:
                return False

        return True

    low = min(B)
    high = sum(B)
    while (low <= high):
        mid = low + (high - low) // 2
        if check(mid) == False:
            low = mid + 1
        else:
            ans = mid
            high = mid - 1
    return ans