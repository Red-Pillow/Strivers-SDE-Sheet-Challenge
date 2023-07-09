# Prob_link: https://www.codingninjas.com/studio/problems/size-of-largest-bst-in-binary-tree_8230743?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

'''
   ------- Binary Tree node structure -------
           class TreeNode :
               def __init__(self, data) :
                   self.data = data
                   self.left = None
                   self.right = None
'''


def fun(root):
    if root == None:
        return 0, float('-inf'), float('inf')

    l_tree = fun(root.left)
    r_tree = fun(root.right)

    # Check the largest from the left subtree,
    # check the smallest from the right subtree anc
    # Compare the values with the root node
    if l_tree[1] < root.data < r_tree[2]:

        # Increase the count, change the largest value
        # and the smallest value
        count = 1 + l_tree[0] + r_tree[0]
        lar = max(l_tree[1], r_tree[1], root.data)
        sma = min(l_tree[2], r_tree[2], root.data)

    # If there is any violation of Binary Search Tree
    else:
        count = max(l_tree[0], r_tree[0])
        lar = float('inf')
        sma = float('-inf')

    return count, lar, sma


def largestBST(root):
    # Write your code here.
    out = fun(root)
    return out[0]