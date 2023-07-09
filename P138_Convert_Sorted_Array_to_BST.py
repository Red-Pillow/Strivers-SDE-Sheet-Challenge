# Prob_link: https://www.codingninjas.com/studio/problems/convert-sorted-array-to-bst_8230836?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right


def sortedArrToBST(arr, n):
    def solve(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(arr[mid])
        root.left = solve(left, mid - 1)
        root.right = solve(mid + 1, right)
        return root

    return solve(0, len(arr) - 1)