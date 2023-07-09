# Prob_link: https://www.codingninjas.com/studio/problems/boundary-traversal-of-binary-tree_8230712?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def left(root,ans):
    if root==None or (root.left==None and root.right==None):
        return
    if root.left:
        ans.append(root.data)
        left(root.left,ans)
    else:
        ans.append(root.data)
        left(root.right,ans)

def leaf(root,ans):
    if root==None:
        return
    if root.left==None and root.right==None:
        ans.append(root.data)
    leaf(root.left,ans)
    leaf(root.right,ans)

def right(root,ans):
    if root==None or(root.left==None and root.right==None):
        return
    if root.right:
        right(root.right,ans)
        ans.append(root.data)
    else:
        right(root.left,ans)
        ans.append(root.data)
def traverseBoundary(root):
    # Write your code here.
    ans=[]
    if root==None:
        return ans
    ans.append(root.data)
    left(root.left,ans)
    leaf(root.left,ans)
    leaf(root.right,ans)
    right(root.right,ans)
    return ans