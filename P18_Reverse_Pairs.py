# Prob_link: https://www.codingninjas.com/codestudio/problems/reverse-pairs_8230825?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *
from bisect import *
def reversePairs(arr, n):
    # Write your code here.
    count = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if i<j and arr[i]>2*arr[j]:
                count+=1
    return count