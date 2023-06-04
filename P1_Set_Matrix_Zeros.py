# code_link: https://www.codingninjas.com/codestudio/problems/set-matrix-zeros_8230862?challengeSlug=striver-sde-challenge&leftPanelTab=0

from math import *
from collections import *
from sys import *
from os import *

from typing import List


def setZeros(matrix: List[List[int]]) -> None:
    # Write your code here.
    zero = 1
    r = len(matrix)
    c = len(matrix[0])

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                if i != 0:
                    matrix[i][0] = 0
                else:
                    zero = 0

    for i in reversed(range(r)):
        for j in reversed(range(c)):
            if i == 0:
                matrix[i][j] *= zero
            elif matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
    return matrix

