# Prob_link: https://www.codingninjas.com/studio/problems/floor-in-bst_8230753?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def fun(root, val):
    floor = -1

    while root:
        if root.data == val:
            return root.data

        elif root.data > val:
            root = root.left

        else:
            floor = root.data
            root = root.right

    return floor


def floorInBST(root, X):
    # Write your Code here.

    return fun(root, X)

