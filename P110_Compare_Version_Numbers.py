# prob_link: https://www.codingninjas.com/studio/problems/compare-version-numbers_8230793?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *


def compareVersions(version1, version2):
    # Write your code here
    a = list(map(int, version1.split('.')))
    b = list(map(int, version2.split('.')))
    N = -1

    posj = -1
    for i in range(len(a) - 1, -1, -1):
        if a[i] != 0:
            posj = i
            break
    if posj > -1:
        a = a[:posj + 1]
    posk = -1
    for i in range(len(b) - 1, -1, -1):
        if b[i] != 0:
            posk = i
            break
    if posk > -1:
        b = b[:posk + 1]

    la = len(a)
    lb = len(b)

    for i in range(min(la, lb)):
        if a[i] > b[i]:
            return (1)
        elif a[i] < b[i]:
            return (-1)
    if a == b:
        return (0)
    elif la > lb:
        s = sum(a[N + 1:])
        if s > 0:
            return (1)
        else:
            return (0)
    elif la < lb:
        s = sum(b[N + 1:])
        if s > 0:
            return (-1)
        else:
            return (0)