# prob_link: https://www.codingninjas.com/studio/problems/lca-of-binary-tree_8230760?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *


# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lowestCommonAncestor(root, x, y):
    # Write your code here.
    if root == None:
        return -1
    if root.data == x or root.data == y:
        return root.data
    left = lowestCommonAncestor(root.left, x, y)
    right = lowestCommonAncestor(root.right, x, y)

    if left == -1:
        return right
    elif right == -1:
        return left
    else:
        return root.data