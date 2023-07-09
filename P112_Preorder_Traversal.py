# Prob_link:  https://www.codingninjas.com/studio/problems/preorder-traversal_8230856?challengeSlug=striver-sde-challenge&leftPanelTab=0

from os import *
from sys import *
from collections import *
from math import *

'''    Following is the Binary Tree node structure:    class TreeNode:      def __init__(self, data=0, left=None, right=None):          self.data = data          self.left = left          self.right = right '''
def preorder(root,ans):
	if root:
		ans.append(root.data)
		preorder(root.left,ans)
		preorder(root.right,ans)

def getPreOrderTraversal(root):    # Write your code here.
	ans=[]
	preorder(root,ans)
	return ans