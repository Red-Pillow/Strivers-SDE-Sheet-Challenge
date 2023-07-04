# prob_link: https://www.codingninjas.com/studio/problems/inorder-traversal_8230857?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

'''
    Following is the Binary Tree node structure:
    class TreeNode:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
'''


def getInOrderTraversal(root):
    # Write your code here.
    res = []
    def traverse(root):
        if root==None:
            return
        traverse(root.left)
        res.append(root.data)
        traverse(root.right)
    traverse(root)
    return res
