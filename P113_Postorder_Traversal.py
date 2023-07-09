# Prob_link:  https://www.codingninjas.com/studio/problems/postorder-traversal_8230858?challengeSlug=striver-sde-challenge&leftPanelTab=0

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

def postorder(root,ans):
    if root:
        postorder(root.left,ans)
        postorder(root.right,ans)
        ans.append(root.data)
def getPostOrderTraversal(root):
    # Write your code here.
    ans=[]
    postorder(root,ans)
    return ans