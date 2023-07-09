# Prob_link: https://www.codingninjas.com/studio/problems/is-height-balanced-binary-tree_8230771?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''


def isBalancedBT(root):
    # Write your code here
    # Return True/False
    def height(root):
        if root == None:
            return 0
        left = height(root.left)
        right = height(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    if height(root) == -1:
        return False
    return True