# prob link: https://www.codingninjas.com/codestudio/problems/pascal-s-triangle_8230805?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

def printPascal(numRows:int):
    # Write your code here.
    # Return a list of lists.
    p = []
    p.append([1])
    for i in range(1,numRows):
        m = len(p[-1])
        temp = []
        temp.append(1)
        last = p[-1]
        for j in range(1,m):
            temp.append(last[j]+last[j-1])
        temp.append(1)
        p.append(temp)
    return p
